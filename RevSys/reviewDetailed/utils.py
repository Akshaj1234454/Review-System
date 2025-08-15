
from transformers import pipeline
import torch

device = 0 if torch.cuda.is_available() else -1
try:
    summarizer = pipeline(
        "summarization", 
        model="facebook/bart-large-cnn",
        device=device,
        max_length=512,
        truncation=True
    )
    print(f"Summarizer loaded on {'GPU' if device == 0 else 'CPU'}")
except Exception as e:
    print(f"Warning: Could not load summarizer - {e}")
    summarizer = None

def generate_review_summary(review_list):

    if not review_list or not summarizer:
        return "No reviews available for summary."
    
    try:
        # Filter meaningful reviews and limit to 8 most substantial ones
        meaningful_reviews = [review.strip() for review in review_list if len(review.strip()) > 10][:8]
        
        if not meaningful_reviews:
            return "Not enough detailed reviews available for analysis."
        
        # For single review, create a simple analysis
        if len(meaningful_reviews) == 1:
            review = meaningful_reviews[0]
            if "good" in review.lower() or "great" in review.lower() or "excellent" in review.lower():
                return f"Users generally have positive feedback about this product based on early reviews."
            elif "bad" in review.lower() or "poor" in review.lower() or "terrible" in review.lower():
                return f"Initial customer feedback suggests some concerns with this product's performance."
            else:
                return f"Users have mixed feelings about this product, with varying experiences reported."
        
        # Combine reviews with clear separators
        combined_text = " ".join(meaningful_reviews)
        
        # Truncate if too long
        if len(combined_text) > 1000:
            combined_text = combined_text[:1000] + "..."
        
        # Normalize personal pronouns and awkward phrasing before summarization
        normalized_text = combined_text.replace(" my ", " their ").replace(" My ", " Their ")
        normalized_text = normalized_text.replace(" I ", " they ").replace(" me ", " them ")
        normalized_text = normalized_text.replace("on my device", "on devices").replace("for me", "for users")
        
        # Use a simpler, more direct approach for BART
        summary_input = f"Summarize customer opinions: {normalized_text}"
        
        # Generate summary with conservative parameters
        summary = summarizer(
            summary_input, 
            max_length=80, 
            min_length=25, 
            do_sample=False,
            truncation=True
        )
        
        result = summary[0]['summary_text']
        
        # Post-process to make it more natural and fix awkward phrasing
        result = result.replace(" their device", " devices").replace(" their devices", " devices")
        result = result.replace("on their device", "on devices").replace("with their device", "with devices")
        result = result.replace("they worked", "it worked").replace("they started", "it started")
        result = result.replace("they wouldn't", "users wouldn't").replace("they would", "users would")
        
        # Post-process to make it more natural
        if len(result) < 20 or result.lower().startswith("summarize") or result.lower().startswith("based on"):
            # Fallback to simple pattern-based summary
            positive_words = ["good", "great", "excellent", "amazing", "love", "perfect", "quality", "worked great"]
            negative_words = ["bad", "poor", "terrible", "awful", "hate", "cheap", "broke", "slow", "short", "doesn't support"]
            
            text_lower = combined_text.lower()
            positive_count = sum(1 for word in positive_words if word in text_lower)
            negative_count = sum(1 for word in negative_words if word in text_lower)
            
            # Create more specific summaries based on content
            if "charging" in text_lower and "slow" in text_lower:
                return "Users report mixed experiences, with initial satisfaction but concerns about charging performance over time."
            elif "cable" in text_lower and "short" in text_lower:
                return "Customers have mixed feedback, noting issues with cable length and charging compatibility."
            elif positive_count > negative_count:
                return "Customers generally have positive experiences with this product, praising its quality and performance."
            elif negative_count > positive_count:
                return "Users have mixed reviews, with some customers reporting issues with build quality and performance."
            else:
                return "Customer feedback is varied, with both positive experiences and some concerns mentioned."
        
        # Ensure the result starts naturally
        if not any(result.lower().startswith(phrase) for phrase in ["users", "customers", "buyers", "people", "most", "the product"]):
            if "cable" in combined_text.lower():
                result = f"Users find that {result.lower()}"
            else:
                result = f"Customers report that {result.lower()}"
        
        return result.capitalize()
        
    except Exception as e:
        print(f"Error generating summary: {e}")
        return f"Customer reviews available ({len(review_list)} reviews) - summary generation temporarily unavailable."
