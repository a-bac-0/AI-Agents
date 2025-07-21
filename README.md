# Social Media Scheduler Multi-Agent System

## AI Agents for Content Automation

### 1. Brief History & Evolution of AI Agents

- **Early Agents (pre-2010):** Rule-based, expert systems, limited adaptability.
- **Deep Learning Era (2015–2020):** Single-task agents, improved NLP, image generation.
- **LLMs & Tool Use (2021–2023):** Agents with reasoning, memory, and tool access (OpenAI, Huggingface, local models).
- **Multi-Agent Systems (2023–2025):** Collaboration, specialization, frameworks like CrewAI, LangChain, LangGraph, RAG, guardrails, knowledge graphs.
- **Current Direction:** Open-source LLMs (Ollama), local models, agent frameworks, cost-effective/free solutions, extensibility.

### 2. Project Overview

**Goal:** Build a multi-agent system to automate content generation, review, and scheduling for social media platforms (Blog, Twitter/X, Instagram, LinkedIn).

- **Agents:**
  - Content Generator Agent (LLM, prompt engineering)
  - Reviewer Agent (quality, guardrails)
  - Scheduler Agent (publishing workflow)
  - (Optional) Image Generator Agent (free APIs)
- **Tech Stack:** Python, LangChain, CrewAI, Streamlit (UI), Ollama (local LLMs), Huggingface, free image APIs
- **Extensible:** Easily add new platforms, agents, or tools

### 3. Practical Activity

**Task:**

- Use the provided code to run a Streamlit app
- Generate, review, and schedule posts for different platforms
- Experiment with prompts, agent roles, and workflows
- Extend with new agents or platforms

### 4. Setup & Usage

#### Requirements

- Python 3.10+
- [Ollama](https://ollama.com/) (for local LLMs)
- [Streamlit](https://streamlit.io/)
- [LangChain](https://python.langchain.com/)
- [CrewAI](https://docs.crewai.com/)
- (Optional) Huggingface Transformers

#### Installation

```bash
# Clone the repo
git clone https://github.com/a-bac-0/AI-Agents.git
cd ai_agents
# Install dependencies
pip install -r requirements.txt
# Start Ollama (see docs)
# Run the app
streamlit run src/app.py
```

#### Usage

- Enter your prompts for text and image generation separately in the app.
- Select the platform and image source (Unsplash recommended for reliability).
- Generate content and images independently.
- Review/edit output.
- Schedule for publishing (demo: simulated scheduling).

#### Troubleshooting & Fixes

- **Ollama timeout:** If text generation fails or times out, increase the timeout in `agents.py` (now set to 120 seconds). Use simple prompts and check Ollama logs if issues persist.
- **Image not found (Unsplash):** Try more general keywords or check your Unsplash API key. The app now shows a warning if no image is found.
- **Huggingface image generation:** Can be slow on CPU or fail if RAM is low. Use simple prompts and check for error messages in the app.
- **Separate prompts:** The app now uses separate fields for text and image prompts to avoid mismatches and improve reliability.

#### Instagram Integration (Demo)

You can post generated content and images to Instagram using the unofficial `instagrapi` library:

1. Install instagrapi:
   ```bash
   pip install instagrapi
   ```
2. Save your generated image locally (Unsplash: download the URL, Huggingface: already saved).
3. Use the following script to post to Instagram:

   ```python
   import requests
   from instagrapi import Client

   # Save image from URL
   image_url = "YOUR_IMAGE_URL_HERE"
   image_path = "generated_image.jpg"
   response = requests.get(image_url)
   with open(image_path, "wb") as f:
       f.write(response.content)

   # Prepare caption
   caption = "YOUR_GENERATED_CAPTION_HERE"

   # Login and post
   cl = Client()
   cl.login("your_username", "your_password")
   cl.photo_upload(image_path, caption)
   ```

4. Replace the placeholders with your actual image URL, caption, and Instagram credentials.
5. For Huggingface images, use the local file path directly.

**Note:** This method is for educational/demo use only. Instagram may require verification on first login.

### 5. Repo Structure

```
README.md
src/
  app.py           # Streamlit UI
  agents.py        # Agent definitions (generator, reviewer, scheduler)
  prompts.py       # Prompt templates
  utils.py         # Helper functions
requirements.txt
```

### 6. Extension Ideas

- Add more platforms or agent roles
- Integrate real scheduling APIs
- Add RAG for news/scientific content
- Multi-language support
- Guardrails for quality/alignment

### 7. References & Further Reading

- [LangChain](https://python.langchain.com/)
- [CrewAI](https://docs.crewai.com/)
- [Ollama](https://ollama.com/)
- [Streamlit](https://streamlit.io/)
- [Huggingface](https://huggingface.co/)
- [Roadmap Mad AI P4](https://roadmap-mad-ai-p4.coderf5.es)

---

**For questions or contributions, open an issue or pull request!**
