"""
Streamlit UI for Social Media Scheduler Multi-Agent System
"""

import streamlit as st
from agents import ContentGeneratorAgent, ReviewerAgent, SchedulerAgent, ImageGeneratorAgent
from prompts import PROMPTS
from utils import get_platforms, format_output


st.title("Social Media Scheduler Multi-Agent Demo")


# --- UI Section ---
# Platform selection for content
platform = st.selectbox("Choose platform", get_platforms())
# --- Prompt for text generation (Ollama) ---
text_prompt = st.text_input("Text Prompt (for content generation)")
# --- Prompt for image generation (Unsplash/Huggingface/Ollama) ---
image_prompt = st.text_input("Image Prompt (for image generation)")
# Audience for text generation
audience = st.text_input("Audience")
# Scheduling time
time = st.text_input("Schedule time (e.g., 2025-07-18 10:00)")
# Image source selection (independent from text)
image_source = st.selectbox("Image Source for Images", ["Unsplash", "Huggingface", "Ollama"])
# Unsplash API key (only needed for Unsplash)
unsplash_access_key = st.text_input("Unsplash Access Key (for Unsplash)", type="password")


# --- Main Logic Section ---
if st.button("Generate & Schedule"):
    # --- Text Generation (Ollama) ---
    generator = ContentGeneratorAgent(model="llama2")
    # Use the text prompt for content generation
    content = generator.generate(text_prompt, audience, platform)

    # --- Review Agent ---
    reviewer = ReviewerAgent()
    review = reviewer.review(content)

    # --- Image Generation (user selects source independently) ---
    image_url = None
    if platform in ["instagram", "blog"]:
        # Only generate images for platforms that support them
        image_agent = ImageGeneratorAgent(
            unsplash_access_key=unsplash_access_key,
            image_source=image_source
        )
        # Use the image prompt for image generation
        image_url = image_agent.generate_image(image_prompt)

    # --- Scheduling Agent ---
    scheduler = SchedulerAgent()
    scheduled = scheduler.schedule(content, platform, time)

    # --- Display Results ---
    st.subheader("Generated Content (Text)")
    st.write(review["content"])

    st.subheader("Generated Image")
    if image_url:
        st.image(image_url, caption=f"Image for {image_prompt}")
    else:
        st.warning("No image found for this image prompt. Try a more general keyword or check your Unsplash API key.")

    st.subheader("Review Feedback")
    st.write(review["feedback"])

    st.subheader("Scheduling Result")
    st.write(scheduled)

# --- End of App ---
