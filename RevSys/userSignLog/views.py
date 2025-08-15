from django.shortcuts import redirect, render
from .forms import SignUpForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
import torch
device = 0 if torch.cuda.is_available() else -1
#summarizer = pipeline("summarization", model="facebook/bart-large-cnn", device=device)
print("Using GPU" if device == 0 else "Using CPU")

def summarize_reviews_free(reviews):
    review_text = "\n".join(f"- {review}" for review in reviews[:5])

    prompt = (
        "Summarize the following product reviews in one sentence from a neutral, third-person perspective. "
        "Avoid repeating reviews verbatim. Focus only on overall trends regarding build quality, charging speed, durability, and value for money. "
        "If opinions are mixed, say so clearly (e.g., 'Buyers are mixed: they appreciate X but dislike Y'). "
        "Keep it concise, informative, and balanced.\n\n"
        f"{review_text}"
)
    

    # Truncate if needed
    text = " ".join(prompt.split()[:512])

    gs = globals().get('summarizer')
    if gs:
        summary = gs(text, max_length=150, min_length=60, do_sample=False)
        return summary[0]['summary_text']
    return ""



def SignUp(request):
    form = SignUpForm()
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("LogIn")

    data = {
        "form": form,
    }
    return render(request, "SignUp.html", data)


def LogIn(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("index")
        else:
            messages.error(request, "Invalid username or password")

    return render(request, "LogIn.html")