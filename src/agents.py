"""
Agent definitions for Social Media Scheduler Multi-Agent System
"""

from typing import Dict, Any

# Content Generator Agent
import requests
import subprocess

class ContentGeneratorAgent:
    def __init__(self, model="llama2"):
        self.model = model
    def generate(self, topic: str, audience: str, platform: str) -> str:
        # Use Ollama to generate content
        prompt = f"Write a {platform} post about '{topic}' for {audience}."
        try:
            result = subprocess.run([
                "ollama", "run", self.model, prompt
            ], capture_output=True, text=True, timeout=120)
            if result.stdout:
                output = result.stdout.strip()
                if output:
                    return output
                else:
                    return "[Ollama returned no content. Try a different prompt or check your model installation.]"
            else:
                return f"[Ollama did not return any output. Check Ollama logs or try a different model.]"
        except Exception as e:
            return f"[Error generating content: {e}]"

# Reviewer Agent
class ReviewerAgent:
    def review(self, content: str) -> Dict[str, Any]:
        # Simple guardrails: check length, basic quality
        feedback = "Looks good!"
        if len(content) < 20:
            feedback = "Content too short."
        return {"content": content, "feedback": feedback}

# Scheduler Agent
class SchedulerAgent:
    def schedule(self, content: str, platform: str, time: str) -> str:
        # Simulate scheduling
        return f"Scheduled for {platform} at {time}: {content[:30]}..."

# Image Generator Agent
class ImageGeneratorAgent:
    def __init__(self, unsplash_access_key=None, image_source="Unsplash"):
        self.unsplash_access_key = unsplash_access_key
        self.image_source = image_source

    def generate_image(self, prompt: str) -> str:
        if self.image_source == "Unsplash":
            if not self.unsplash_access_key:
                return None
            url = f"https://api.unsplash.com/photos/random?query={prompt}&client_id={self.unsplash_access_key}"
            try:
                response = requests.get(url)
                data = response.json()
                image_url = data.get("urls", {}).get("regular")
                return image_url
            except Exception as e:
                return None
        elif self.image_source == "Huggingface":
            # Huggingface Stable Diffusion integration (returns local file path)
            import time
            start_time = time.time()
            try:
                from diffusers import StableDiffusionPipeline
                import torch
                pipe = StableDiffusionPipeline.from_pretrained("runwayml/stable-diffusion-v1-5")
                pipe = pipe.to("cpu")
                image_result = pipe(prompt)
                elapsed = time.time() - start_time
                if elapsed > 60:
                    return f"[Image generation took too long ({int(elapsed)}s). Try a simpler prompt or use a GPU.]"
                if hasattr(image_result, 'images') and image_result.images:
                    image = image_result.images[0]
                    image_path = f"generated_{prompt.replace(' ','_')}.png"
                    image.save(image_path)
                    return image_path
                else:
                    return "[Huggingface did not return an image. Try a simpler prompt or check your setup.]"
            except Exception as e:
                import traceback
                print(traceback.format_exc())
                return f"[Error generating image with Huggingface: {e}]"
        elif self.image_source == "Ollama":
            # Ollama image model integration (if available)
            try:
                result = subprocess.run([
                    "ollama", "run", "llava", prompt
                ], capture_output=True, text=True, timeout=60)
                # Assume Ollama returns a path or URL to the image
                return result.stdout.strip()
            except Exception as e:
                return None
        return None
