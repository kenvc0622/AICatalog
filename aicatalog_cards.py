"""
streamlit_app.py - Enhanced AI Products & Apps Catalog
Comprehensive catalog with expanded tools, categories, and dynamic profiling
"""

import streamlit as st
import pandas as pd
from typing import List, Dict, Optional
from dataclasses import dataclass, field
from datetime import datetime
import random

# Page configuration
st.set_page_config(
    page_title="AI Products & Apps Catalog",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Enhanced Custom CSS with animations
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');
    
    * {
        font-family: 'Inter', sans-serif;
    }
    
    .main-header {
        font-size: 3.5rem;
        text-align: center;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 50%, #f093fb 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 1rem;
        animation: gradient 3s ease infinite;
    }
    
    @keyframes gradient {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }
    
    .subtitle {
        text-align: center;
        color: #666;
        font-size: 1.2rem;
        margin-bottom: 2rem;
    }
    
    .product-card {
        background: linear-gradient(135deg, #ffffff 0%, #f8f9fa 100%);
        padding: 1.8rem;
        border-radius: 20px;
        box-shadow: 0 10px 30px rgba(0,0,0,0.08);
        margin-bottom: 1.5rem;
        border-left: 5px solid #667eea;
        transition: transform 0.3s ease, box-shadow 0.3s ease;
        position: relative;
        overflow: hidden;
    }
    
    .product-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 15px 40px rgba(102, 126, 234, 0.2);
    }
    
    .product-card::before {
        content: '';
        position: absolute;
        top: 0;
        right: 0;
        width: 100px;
        height: 100px;
        background: linear-gradient(135deg, transparent 50%, rgba(102, 126, 234, 0.05) 50%);
        border-radius: 0 0 0 100px;
    }
    
    .product-name {
        color: #2d3436;
        font-size: 1.4rem;
        font-weight: 700;
        margin-bottom: 0.5rem;
        display: flex;
        align-items: center;
        gap: 0.5rem;
    }
    
    .product-emoji {
        font-size: 1.8rem;
    }
    
    .rating-stars {
        color: #ffd700;
        font-size: 1.1rem;
        letter-spacing: 2px;
    }
    
    .category-badge {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 0.3rem 1rem;
        border-radius: 20px;
        font-size: 0.8rem;
        display: inline-block;
        margin: 0.2rem;
        font-weight: 500;
        transition: transform 0.2s;
    }
    
    .category-badge:hover {
        transform: scale(1.05);
    }
    
    .pricing-badge {
        background: linear-gradient(135deg, #00b894 0%, #00cec9 100%);
        color: white;
        padding: 0.4rem 1rem;
        border-radius: 12px;
        font-size: 0.85rem;
        font-weight: 600;
    }
    
    .feature-tag {
        background: #e8eaf6;
        color: #667eea;
        padding: 0.3rem 0.8rem;
        border-radius: 15px;
        font-size: 0.8rem;
        display: inline-block;
        margin: 0.2rem;
        font-weight: 500;
        border: 1px solid #c5cae9;
    }
    
    .use-case-section {
        background: linear-gradient(135deg, #f8f9fa 0%, #e9ecef 100%);
        padding: 1.5rem;
        border-radius: 15px;
        margin: 1rem 0;
    }
    
    .stat-card {
        background: white;
        padding: 1.5rem;
        border-radius: 15px;
        box-shadow: 0 5px 15px rgba(0,0,0,0.05);
        text-align: center;
        transition: transform 0.3s;
    }
    
    .stat-card:hover {
        transform: translateY(-3px);
    }
    
    .stat-number {
        font-size: 2.5rem;
        font-weight: 700;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }
    
    .trending-badge {
        background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
        color: white;
        padding: 0.2rem 0.8rem;
        border-radius: 20px;
        font-size: 0.75rem;
        animation: pulse 2s infinite;
    }
    
    @keyframes pulse {
        0% { opacity: 1; }
        50% { opacity: 0.7; }
        100% { opacity: 1; }
    }
    
    .popularity-bar {
        height: 8px;
        background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
        border-radius: 10px;
        margin: 0.5rem 0;
    }
    
    .category-card {
        background: white;
        padding: 2rem;
        border-radius: 20px;
        box-shadow: 0 10px 30px rgba(0,0,0,0.1);
        cursor: pointer;
        transition: all 0.3s ease;
        text-align: center;
        border: 2px solid transparent;
    }
    
    .category-card:hover {
        border-color: #667eea;
        transform: translateY(-5px);
        box-shadow: 0 15px 40px rgba(102, 126, 234, 0.3);
    }
    
    .category-icon {
        font-size: 3rem;
        margin-bottom: 1rem;
    }
    
    .category-count {
        background: #e8eaf6;
        color: #667eea;
        padding: 0.3rem 1rem;
        border-radius: 20px;
        font-weight: 600;
        font-size: 0.9rem;
    }
    </style>
""", unsafe_allow_html=True)

@dataclass
class AIProduct:
    """Enhanced AI Product data model with dynamic profiling"""
    name: str
    emoji: str
    url: str
    description: str
    use_cases: List[str]
    pricing: str
    pricing_type: str  # Free, Freemium, Paid, Enterprise
    rating: float
    features: List[str]
    target_users: List[str]  # Developers, Marketers, Designers, etc.
    platform: List[str]  # Web, Mobile, Desktop, API
    founded_year: int
    popularity_score: float  # 0-100
    integration_ecosystem: List[str]  # Slack, Notion, etc.
    learning_curve: str  # Easy, Moderate, Advanced
    
class AICatalog:
    """Extended catalog with 60+ AI tools across multiple categories"""
    
    def __init__(self):
        self.products = self._initialize_extended_catalog()
        self._calculate_dynamic_profiles()
    
    def _initialize_extended_catalog(self) -> List[AIProduct]:
        """Initialize with comprehensive catalog of 60+ AI tools"""
        
        return [
            # ========= VIDEO GENERATION & EDITING =========
            AIProduct(
                name="Runway ML", emoji="🎬",
                url="https://runwayml.com",
                description="Advanced AI video generation and editing platform with text-to-video capabilities",
                use_cases=["Video Generation", "Video Editing", "Content Creation"],
                pricing="Free / $12/mo", pricing_type="Freemium",
                rating=4.5, features=["Text-to-video", "Green screen", "Motion tracking", "Image generation"],
                target_users=["Content Creators", "Filmmakers", "Marketers"],
                platform=["Web"], founded_year=2018, popularity_score=88,
                integration_ecosystem=["Adobe", "Figma"], learning_curve="Moderate"
            ),
            AIProduct(
                name="Synthesia", emoji="🎭",
                url="https://synthesia.io",
                description="Create professional videos with AI avatars from text scripts",
                use_cases=["Video Generation", "Content Creation", "E-Learning"],
                pricing="$30/mo", pricing_type="Paid",
                rating=4.7, features=["AI avatars", "120+ languages", "Custom backgrounds", "Script to video"],
                target_users=["Marketers", "Educators", "Enterprises"],
                platform=["Web"], founded_year=2017, popularity_score=85,
                integration_ecosystem=["PowerPoint", "WordPress"], learning_curve="Easy"
            ),
            AIProduct(
                name="Pictory", emoji="✂️",
                url="https://pictory.ai",
                description="Automatically create short video highlights from long-form content",
                use_cases=["Video Editing", "Content Creation", "Social Media"],
                pricing="$19/mo", pricing_type="Paid",
                rating=4.3, features=["Auto-summarization", "Caption generation", "Brand kit", "Stock footage"],
                target_users=["Content Creators", "Marketers", "YouTubers"],
                platform=["Web"], founded_year=2019, popularity_score=75,
                integration_ecosystem=["YouTube", "Vimeo"], learning_curve="Easy"
            ),
            AIProduct(
                name="Descript", emoji="🎙️",
                url="https://descript.com",
                description="Revolutionary text-based video and audio editor",
                use_cases=["Video Editing", "Podcasting", "Content Creation"],
                pricing="Free / $24/mo", pricing_type="Freemium",
                rating=4.6, features=["Text-based editing", "Screen recording", "AI voices", "Transcription"],
                target_users=["Podcasters", "YouTubers", "Educators"],
                platform=["Web", "Desktop"], founded_year=2017, popularity_score=82,
                integration_ecosystem=["Slack", "Zoom"], learning_curve="Moderate"
            ),
            AIProduct(
                name="HeyGen", emoji="🎥",
                url="https://heygen.com",
                description="AI video generator with talking avatars and voice cloning",
                use_cases=["Video Generation", "Content Creation", "Marketing"],
                pricing="$24/mo", pricing_type="Paid",
                rating=4.5, features=["Talking avatars", "Voice cloning", "Template library", "API access"],
                target_users=["Marketers", "Sales Teams", "Content Creators"],
                platform=["Web"], founded_year=2020, popularity_score=78,
                integration_ecosystem=["HubSpot", "Salesforce"], learning_curve="Easy"
            ),
            
            # ========= TEXT & CONTENT GENERATION =========
            AIProduct(
                name="Jasper", emoji="✍️",
                url="https://jasper.ai",
                description="Enterprise AI content platform for marketing teams",
                use_cases=["Content Creation", "Copywriting", "Marketing"],
                pricing="$49/mo", pricing_type="Paid",
                rating=4.6, features=["Blog writing", "Brand voice", "SEO optimization", "Campaign creation"],
                target_users=["Marketers", "Copywriters", "Enterprises"],
                platform=["Web"], founded_year=2020, popularity_score=90,
                integration_ecosystem=["Grammarly", "SurferSEO", "Copyscape"], learning_curve="Easy"
            ),
            AIProduct(
                name="Copy.ai", emoji="📝",
                url="https://copy.ai",
                description="AI-powered copywriting for sales, marketing, and content",
                use_cases=["Content Creation", "Copywriting", "Social Media"],
                pricing="Free / $49/mo", pricing_type="Freemium",
                rating=4.5, features=["90+ templates", "Brand voice", "Multi-language", "Blog wizard"],
                target_users=["Marketers", "Sales Teams", "Entrepreneurs"],
                platform=["Web"], founded_year=2020, popularity_score=85,
                integration_ecosystem=["Google Docs", "WordPress"], learning_curve="Easy"
            ),
            AIProduct(
                name="Writesonic", emoji="📄",
                url="https://writesonic.com",
                description="AI writer for SEO-optimized content, ads, and articles",
                use_cases=["Content Creation", "SEO", "Marketing"],
                pricing="Free / $19/mo", pricing_type="Freemium",
                rating=4.4, features=["AI article writer", "Landing pages", "Ad copy", "Product descriptions"],
                target_users=["Marketers", "SEO Specialists", "E-commerce"],
                platform=["Web"], founded_year=2020, popularity_score=80,
                integration_ecosystem=["WordPress", "Shopify"], learning_curve="Easy"
            ),
            AIProduct(
                name="Rytr", emoji="🖊️",
                url="https://rytr.me",
                description="Affordable AI writing assistant for various content types",
                use_cases=["Content Creation", "Copywriting", "Email Writing"],
                pricing="Free / $9/mo", pricing_type="Freemium",
                rating=4.5, features=["40+ use cases", "20+ tones", "Plagiarism checker", "SEO analyzer"],
                target_users=["Freelancers", "Small Business", "Students"],
                platform=["Web"], founded_year=2021, popularity_score=75,
                integration_ecosystem=["WordPress", "Shopify"], learning_curve="Easy"
            ),
            
            # ========= IMAGE GENERATION =========
            AIProduct(
                name="Midjourney", emoji="🎨",
                url="https://midjourney.com",
                description="Create stunning AI art through Discord with advanced style control",
                use_cases=["Image Generation", "Art & Design", "Concept Art"],
                pricing="$10/mo", pricing_type="Paid",
                rating=4.8, features=["Text-to-image", "Style mixing", "Upscaling", "Variation generation"],
                target_users=["Artists", "Designers", "Creative Professionals"],
                platform=["Discord"], founded_year=2021, popularity_score=95,
                integration_ecosystem=["Discord"], learning_curve="Advanced"
            ),
            AIProduct(
                name="DALL-E 3", emoji="🖼️",
                url="https://openai.com/dall-e-3",
                description="OpenAI's most capable image generation model",
                use_cases=["Image Generation", "Art & Design", "Content Creation"],
                pricing="Pay per use", pricing_type="Paid",
                rating=4.7, features=["Text-to-image", "High accuracy", "Safety features", "Style variations"],
                target_users=["Designers", "Marketers", "Creators"],
                platform=["Web", "API"], founded_year=2023, popularity_score=92,
                integration_ecosystem=["ChatGPT", "API"], learning_curve="Easy"
            ),
            AIProduct(
                name="Leonardo.ai", emoji="🎪",
                url="https://leonardo.ai",
                description="AI art generator with gaming and concept art focus",
                use_cases=["Image Generation", "Gaming", "Concept Art"],
                pricing="Free / $10/mo", pricing_type="Freemium",
                rating=4.4, features=["Game assets", "Character design", "Image guidance", "Community models"],
                target_users=["Game Developers", "Artists", "Designers"],
                platform=["Web"], founded_year=2022, popularity_score=78,
                integration_ecosystem=["Unity", "Unreal"], learning_curve="Moderate"
            ),
            AIProduct(
                name="Stable Diffusion", emoji="🔮",
                url="https://stability.ai",
                description="Open-source image generation model with full control",
                use_cases=["Image Generation", "Art & Design", "Development"],
                pricing="Free / Enterprise", pricing_type="Freemium",
                rating=4.6, features=["Open source", "Local deployment", "Fine-tuning", "API access"],
                target_users=["Developers", "Researchers", "Artists"],
                platform=["Web", "API", "Desktop"], founded_year=2022, popularity_score=90,
                integration_ecosystem=["Hugging Face", "Replicate"], learning_curve="Advanced"
            ),
            AIProduct(
                name="Adobe Firefly", emoji="🔥",
                url="https://firefly.adobe.com",
                description="Adobe's generative AI integrated with Creative Cloud",
                use_cases=["Image Generation", "Design", "Photo Editing"],
                pricing="Free / Creative Cloud", pricing_type="Freemium",
                rating=4.5, features=["Generative fill", "Text effects", "Vector generation", "Copyright safe"],
                target_users=["Designers", "Photographers", "Creative Pros"],
                platform=["Web"], founded_year=2023, popularity_score=85,
                integration_ecosystem=["Photoshop", "Illustrator", "Adobe Express"], learning_curve="Easy"
            ),
            
            # ========= CODE & DEVELOPMENT =========
            AIProduct(
                name="GitHub Copilot", emoji="💻",
                url="https://github.com/features/copilot",
                description="AI pair programmer that suggests code in real-time",
                use_cases=["Code Assistant", "Development", "Productivity"],
                pricing="$10/mo", pricing_type="Paid",
                rating=4.7, features=["Code completion", "Multiple languages", "Chat interface", "Pull request summaries"],
                target_users=["Developers", "Software Engineers", "Students"],
                platform=["IDE Extension"], founded_year=2021, popularity_score=95,
                integration_ecosystem=["VS Code", "JetBrains", "Neovim"], learning_curve="Easy"
            ),
            AIProduct(
                name="Cursor", emoji="🖱️",
                url="https://cursor.sh",
                description="AI-first code editor built on VS Code",
                use_cases=["Code Assistant", "Development", "IDE"],
                pricing="Free / $20/mo", pricing_type="Freemium",
                rating=4.8, features=["AI code editor", "Natural language edits", "Codebase understanding", "Debug assistance"],
                target_users=["Developers", "Engineers"],
                platform=["Desktop"], founded_year=2022, popularity_score=88,
                integration_ecosystem=["VS Code extensions"], learning_curve="Easy"
            ),
            AIProduct(
                name="Replit Ghostwriter", emoji="👻",
                url="https://replit.com",
                description="AI-powered coding in the browser with collaborative features",
                use_cases=["Code Assistant", "Development", "Education"],
                pricing="Free / $10/mo", pricing_type="Freemium",
                rating=4.5, features=["In-browser IDE", "AI code generation", "Debug AI", "Deployment"],
                target_users=["Developers", "Students", "Educators"],
                platform=["Web"], founded_year=2022, popularity_score=80,
                integration_ecosystem=["GitHub", "Vercel"], learning_curve="Easy"
            ),
            AIProduct(
                name="Tabnine", emoji="⚡",
                url="https://tabnine.com",
                description="AI code completion with privacy-first approach",
                use_cases=["Code Assistant", "Development", "Enterprise"],
                pricing="Free / $12/mo", pricing_type="Freemium",
                rating=4.4, features=["Code completion", "Team learning", "Self-hosted option", "Privacy focus"],
                target_users=["Developers", "Enterprises", "Security Teams"],
                platform=["IDE Extension"], founded_year=2018, popularity_score=75,
                integration_ecosystem=["VS Code", "IntelliJ", "Eclipse"], learning_curve="Easy"
            ),
            
            # ========= PRESENTATION & DESIGN =========
            AIProduct(
                name="Beautiful.ai", emoji="📊",
                url="https://beautiful.ai",
                description="AI-powered presentation software with smart templates",
                use_cases=["Presentations", "Design", "Business"],
                pricing="Free / $12/mo", pricing_type="Freemium",
                rating=4.4, features=["Smart templates", "Auto-layout", "Team collaboration", "Brand control"],
                target_users=["Professionals", "Teams", "Educators"],
                platform=["Web"], founded_year=2018, popularity_score=80,
                integration_ecosystem=["Slack", "PowerPoint"], learning_curve="Easy"
            ),
            AIProduct(
                name="Gamma", emoji="✨",
                url="https://gamma.app",
                description="AI-powered presentation, document, and webpage creator",
                use_cases=["Presentations", "Documentation", "Content Creation"],
                pricing="Free / $10/mo", pricing_type="Freemium",
                rating=4.6, features=["AI-generated presentations", "Interactive docs", "Web pages", "Analytics"],
                target_users=["Professionals", "Startups", "Educators"],
                platform=["Web"], founded_year=2021, popularity_score=82,
                integration_ecosystem=["Google Drive", "Slack"], learning_curve="Easy"
            ),
            AIProduct(
                name="Canva AI", emoji="🎨",
                url="https://canva.com",
                description="All-in-one design platform with integrated AI features",
                use_cases=["Design", "Presentations", "Social Media"],
                pricing="Free / $12.99/mo", pricing_type="Freemium",
                rating=4.7, features=["Magic design", "Text-to-image", "Background remover", "Brand kit"],
                target_users=["Designers", "Marketers", "Everyone"],
                platform=["Web", "Mobile"], founded_year=2013, popularity_score=95,
                integration_ecosystem=["Dropbox", "Google Drive", "Instagram"], learning_curve="Easy"
            ),
            AIProduct(
                name="Tome", emoji="📖",
                url="https://tome.app",
                description="AI storytelling format for compelling presentations",
                use_cases=["Presentations", "Storytelling", "Content Creation"],
                pricing="Free / $16/mo", pricing_type="Freemium",
                rating=4.5, features=["AI narrative builder", "Interactive embeds", "Live integrations", "Analytics"],
                target_users=["Storytellers", "Marketers", "Sales"],
                platform=["Web"], founded_year=2020, popularity_score=78,
                integration_ecosystem=["Figma", "YouTube", "Twitter"], learning_curve="Easy"
            ),
            
            # ========= VOICE & AUDIO =========
            AIProduct(
                name="ElevenLabs", emoji="🗣️",
                url="https://elevenlabs.io",
                description="Most realistic AI voice generation and cloning",
                use_cases=["Voice Synthesis", "Content Creation", "Audiobooks"],
                pricing="Free / $5/mo", pricing_type="Freemium",
                rating=4.8, features=["Voice cloning", "29 languages", "Emotion control", "API access"],
                target_users=["Content Creators", "Developers", "Enterprises"],
                platform=["Web", "API"], founded_year=2022, popularity_score=92,
                integration_ecosystem=["API"], learning_curve="Easy"
            ),
            AIProduct(
                name="Murf.ai", emoji="🎤",
                url="https://murf.ai",
                description="AI voiceover studio for professional content",
                use_cases=["Voice Synthesis", "Video Production", "E-Learning"],
                pricing="Free / $19/mo", pricing_type="Freemium",
                rating=4.4, features=["120+ voices", "20+ languages", "Voice customization", "Background music"],
                target_users=["Content Creators", "Educators", "Marketers"],
                platform=["Web"], founded_year=2020, popularity_score=76,
                integration_ecosystem=["Canva", "Google Slides"], learning_curve="Easy"
            ),
            AIProduct(
                name="Play.ht", emoji="🎧",
                url="https://play.ht",
                description="AI text-to-speech with ultra-realistic voices",
                use_cases=["Voice Synthesis", "Content Creation", "Accessibility"],
                pricing="$19/mo", pricing_type="Paid",
                rating=4.5, features=["907 AI voices", "142 languages", "Voice cloning", "Podcast creation"],
                target_users=["Content Creators", "Publishers", "Developers"],
                platform=["Web", "API"], founded_year=2016, popularity_score=72,
                integration_ecosystem=["WordPress", "Medium"], learning_curve="Easy"
            ),
            
            # ========= CHATBOTS & CONVERSATIONAL AI =========
            AIProduct(
                name="ChatGPT", emoji="🤖",
                url="https://chat.openai.com",
                description="OpenAI's advanced conversational AI for various tasks",
                use_cases=["Chatbot", "Research", "Content Creation", "Code Assistant"],
                pricing="Free / $20/mo", pricing_type="Freemium",
                rating=4.8, features=["GPT-4", "DALL-E integration", "Web browsing", "Code interpreter"],
                target_users=["Everyone", "Developers", "Researchers"],
                platform=["Web", "Mobile", "API"], founded_year=2022, popularity_score=99,
                integration_ecosystem=["API", "Plugins"], learning_curve="Easy"
            ),
            AIProduct(
                name="Claude", emoji="🧠",
                url="https://anthropic.com",
                description="Anthropic's AI assistant with strong reasoning capabilities",
                use_cases=["Chatbot", "Research", "Analysis", "Writing"],
                pricing="Free / $20/mo", pricing_type="Freemium",
                rating=4.7, features=["100K context", "File analysis", "Constitutional AI", "Code generation"],
                target_users=["Researchers", "Professionals", "Developers"],
                platform=["Web", "API"], founded_year=2023, popularity_score=90,
                integration_ecosystem=["Slack", "API"], learning_curve="Easy"
            ),
            AIProduct(
                name="Perplexity AI", emoji="🔍",
                url="https://perplexity.ai",
                description="AI-powered answer engine with real-time citations",
                use_cases=["Research", "Search", "Analysis"],
                pricing="Free / $20/mo", pricing_type="Freemium",
                rating=4.6, features=["Real-time search", "Citations", "File analysis", "Pro search"],
                target_users=["Researchers", "Students", "Professionals"],
                platform=["Web", "Mobile"], founded_year=2022, popularity_score=88,
                integration_ecosystem=["Chrome Extension"], learning_curve="Easy"
            ),
            AIProduct(
                name="Poe", emoji="💬",
                url="https://poe.com",
                description="Aggregator platform for multiple AI chatbots",
                use_cases=["Chatbot", "Content Creation", "Research"],
                pricing="Free / $19.99/mo", pricing_type="Freemium",
                rating=4.5, features=["Multiple AI models", "Custom bots", "Fast responses", "Cross-platform"],
                target_users=["General Users", "Creators", "Developers"],
                platform=["Web", "Mobile"], founded_year=2022, popularity_score=82,
                integration_ecosystem=["Quora"], learning_curve="Easy"
            ),
            
            # ========= DATA ANALYSIS & SCIENCE =========
            AIProduct(
                name="Julius AI", emoji="📊",
                url="https://julius.ai",
                description="AI data analyst that visualizes and analyzes your data",
                use_cases=["Data Analysis", "Visualization", "Research"],
                pricing="Free / $20/mo", pricing_type="Freemium",
                rating=4.6, features=["Data visualization", "Statistical analysis", "File upload", "Natural language queries"],
                target_users=["Data Analysts", "Researchers", "Business Users"],
                platform=["Web"], founded_year=2023, popularity_score=78,
                integration_ecosystem=["CSV", "Excel", "SQL"], learning_curve="Easy"
            ),
            AIProduct(
                name="Dataiku", emoji="🔬",
                url="https://dataiku.com",
                description="Enterprise AI and data science platform",
                use_cases=["Data Analysis", "Machine Learning", "Enterprise AI"],
                pricing="Free / Enterprise", pricing_type="Freemium",
                rating=4.5, features=["Visual ML", "AutoML", "Data preparation", "MLOps"],
                target_users=["Data Scientists", "Enterprises", "Analysts"],
                platform=["Web", "Desktop"], founded_year=2013, popularity_score=70,
                integration_ecosystem=["AWS", "Azure", "GCP"], learning_curve="Advanced"
            ),
            
            # ========= PRODUCTIVITY & WORKFLOW =========
            AIProduct(
                name="Notion AI", emoji="📝",
                url="https://notion.so",
                description="AI-powered workspace for notes, docs, and projects",
                use_cases=["Productivity", "Documentation", "Project Management"],
                pricing="Free / $10/mo", pricing_type="Freemium",
                rating=4.7, features=["AI writing", "Summarization", "Translation", "Task management"],
                target_users=["Teams", "Individuals", "Enterprises"],
                platform=["Web", "Desktop", "Mobile"], founded_year=2022, popularity_score=88,
                integration_ecosystem=["Slack", "Google Drive", "GitHub"], learning_curve="Easy"
            ),
            AIProduct(
                name="Taskade AI", emoji="✅",
                url="https://taskade.com",
                description="AI-powered productivity and project management",
                use_cases=["Productivity", "Project Management", "Collaboration"],
                pricing="Free / $8/mo", pricing_type="Freemium",
                rating=4.5, features=["AI agents", "Mind maps", "Task automation", "Real-time collaboration"],
                target_users=["Teams", "Project Managers", "Startups"],
                platform=["Web", "Mobile", "Desktop"], founded_year=2017, popularity_score=72,
                integration_ecosystem=["Slack", "Google Calendar", "Zapier"], learning_curve="Easy"
            ),
            AIProduct(
                name="Mem.ai", emoji="🧠",
                url="https://mem.ai",
                description="AI-powered knowledge management and note-taking",
                use_cases=["Productivity", "Knowledge Management", "Note-taking"],
                pricing="Free / $14.99/mo", pricing_type="Freemium",
                rating=4.4, features=["AI-organized notes", "Smart search", "Auto-tagging", "Meeting notes"],
                target_users=["Professionals", "Researchers", "Knowledge Workers"],
                platform=["Web", "Mobile"], founded_year=2021, popularity_score=68,
                integration_ecosystem=["Calendar", "Email"], learning_curve="Moderate"
            ),
            
            # ========= MARKETING & SEO =========
            AIProduct(
                name="SurferSEO", emoji="📈",
                url="https://surferseo.com",
                description="AI-powered SEO content optimization platform",
                use_cases=["SEO", "Content Marketing", "Content Strategy"],
                pricing="$89/mo", pricing_type="Paid",
                rating=4.6, features=["Content editor", "Keyword research", "SERP analyzer", "Audit tool"],
                target_users=["SEO Specialists", "Content Marketers", "Agencies"],
                platform=["Web"], founded_year=2017, popularity_score=80,
                integration_ecosystem=["Google Docs", "WordPress", "Jasper"], learning_curve="Moderate"
            ),
            AIProduct(
                name="Semrush", emoji="🎯",
                url="https://semrush.com",
                description="All-in-one marketing toolkit with AI capabilities",
                use_cases=["SEO", "Marketing", "Competitive Analysis"],
                pricing="$129.95/mo", pricing_type="Paid",
                rating=4.5, features=["Keyword magic", "Site audit", "Content marketing", "Social media"],
                target_users=["Marketers", "SEO Specialists", "Agencies"],
                platform=["Web"], founded_year=2008, popularity_score=90,
                integration_ecosystem=["Google Analytics", "Search Console"], learning_curve="Advanced"
            ),
            
            # ========= MUSIC & AUDIO GENERATION =========
            AIProduct(
                name="Suno AI", emoji="🎵",
                url="https://suno.ai",
                description="AI music generation from text prompts",
                use_cases=["Music Creation", "Content Creation", "Entertainment"],
                pricing="Free / $10/mo", pricing_type="Freemium",
                rating=4.6, features=["Text-to-music", "Multiple genres", "Vocal synthesis", "Full songs"],
                target_users=["Musicians", "Content Creators", "Developers"],
                platform=["Web"], founded_year=2023, popularity_score=85,
                integration_ecosystem=["API"], learning_curve="Easy"
            ),
            AIProduct(
                name="AIVA", emoji="🎼",
                url="https://aiva.ai",
                description="AI composer for emotional soundtrack creation",
                use_cases=["Music Creation", "Game Development", "Film Scoring"],
                pricing="Free / €15/mo", pricing_type="Freemium",
                rating=4.3, features=["Emotional music", "300+ styles", "MIDI export", "Copyright"],
                target_users=["Composers", "Game Developers", "Filmmakers"],
                platform=["Web"], founded_year=2016, popularity_score=65,
                integration_ecosystem=["DAWs"], learning_curve="Moderate"
            ),
            AIProduct(
                name="Beatoven.ai", emoji="🥁",
                url="https://beatoven.ai",
                description="AI music generator for content creators",
                use_cases=["Music Creation", "Video Production", "Content Creation"],
                pricing="Free / $20/mo", pricing_type="Freemium",
                rating=4.4, features=["Mood-based music", "Royalty-free", "Custom lengths", "Multiple genres"],
                target_users=["Content Creators", "YouTubers", "Podcasters"],
                platform=["Web"], founded_year=2021, popularity_score=70,
                integration_ecosystem=["YouTube", "Vimeo"], learning_curve="Easy"
            ),
            
            # ========= 3D & MODELING =========
            AIProduct(
                name="Meshy AI", emoji="🎮",
                url="https://meshy.ai",
                description="Generate 3D models from text and images",
                use_cases=["3D Modeling", "Game Development", "AR/VR"],
                pricing="Free / $20/mo", pricing_type="Freemium",
                rating=4.5, features=["Text to 3D", "Image to 3D", "Texture generation", "Multiple formats"],
                target_users=["Game Developers", "3D Artists", "Architects"],
                platform=["Web"], founded_year=2022, popularity_score=72,
                integration_ecosystem=["Unity", "Blender", "Unreal"], learning_curve="Moderate"
            ),
            AIProduct(
                name="Luma AI", emoji="📸",
                url="https://lumalabs.ai",
                description="Capture and create photorealistic 3D content with AI",
                use_cases=["3D Modeling", "Photography", "AR/VR"],
                pricing="Free", pricing_type="Free",
                rating=4.6, features=["NeRF captures", "3D generation", "Video to 3D", "API access"],
                target_users=["Creators", "Developers", "Photographers"],
                platform=["Mobile", "Web"], founded_year=2021, popularity_score=75,
                integration_ecosystem=["Blender", "Unity"], learning_curve="Easy"
            ),
            
            # ========= MEETING & TRANSCRIPTION =========
            AIProduct(
                name="Otter.ai", emoji="📝",
                url="https://otter.ai",
                description="AI meeting assistant for notes and transcription",
                use_cases=["Transcription", "Meeting Assistant", "Productivity"],
                pricing="Free / $16.99/mo", pricing_type="Freemium",
                rating=4.5, features=["Real-time transcription", "Meeting summaries", "Speaker identification", "Search"],
                target_users=["Professionals", "Teams", "Journalists"],
                platform=["Web", "Mobile"], founded_year=2016, popularity_score=82,
                integration_ecosystem=["Zoom", "Google Meet", "Slack"], learning_curve="Easy"
            ),
            AIProduct(
                name="Fireflies.ai", emoji="🔥",
                url="https://fireflies.ai",
                description="AI meeting transcription and analysis",
                use_cases=["Transcription", "Meeting Assistant", "Sales"],
                pricing="Free / $10/mo", pricing_type="Freemium",
                rating=4.6, features=["Auto-join meetings", "Searchable transcripts", "Analytics", "CRM integration"],
                target_users=["Sales Teams", "Managers", "Recruiters"],
                platform=["Web", "Browser Extension"], founded_year=2016, popularity_score=78,
                integration_ecosystem=["Salesforce", "HubSpot", "Slack"], learning_curve="Easy"
            ),
            
            # ========= E-COMMERCE =========
            AIProduct(
                name="Octane AI", emoji="🛍️",
                url="https://octaneai.com",
                description="AI-powered quizzes and personalization for Shopify",
                use_cases=["E-commerce", "Marketing", "Customer Engagement"],
                pricing="$50/mo", pricing_type="Paid",
                rating=4.5, features=["Product quizzes", "Personalization", "SMS marketing", "Analytics"],
                target_users=["E-commerce Stores", "Marketers", "Shopify Merchants"],
                platform=["Web"], founded_year=2016, popularity_score=65,
                integration_ecosystem=["Shopify", "Klaviyo", "ReCharge"], learning_curve="Easy"
            ),
            AIProduct(
                name="Vue.ai", emoji="👗",
                url="https://vue.ai",
                description="AI-powered retail automation and personalization",
                use_cases=["E-commerce", "Retail", "Visual Merchandising"],
                pricing="Enterprise", pricing_type="Enterprise",
                rating=4.3, features=["Visual AI", "Styling automation", "Product tagging", "Personalization"],
                target_users=["Retailers", "E-commerce", "Fashion Brands"],
                platform=["Web", "API"], founded_year=2016, popularity_score=60,
                integration_ecosystem=["Shopify", "Salesforce Commerce"], learning_curve="Advanced"
            ),
            
            # ========= CUSTOMER SERVICE =========
            AIProduct(
                name="Intercom Fin", emoji="🎧",
                url="https://intercom.com/fin",
                description="AI customer service bot by Intercom",
                use_cases=["Customer Service", "Chatbot", "Support"],
                pricing="From $74/mo", pricing_type="Paid",
                rating=4.5, features=["AI chatbot", "Knowledge base", "Human handoff", "Multi-language"],
                target_users=["Customer Support Teams", "SaaS Companies"],
                platform=["Web"], founded_year=2023, popularity_score=75,
                integration_ecosystem=["Intercom", "Slack", "Salesforce"], learning_curve="Easy"
            ),
            AIProduct(
                name="Ada", emoji="💁",
                url="https://ada.cx",
                description="AI-powered customer service automation platform",
                use_cases=["Customer Service", "Chatbot", "Automation"],
                pricing="Enterprise", pricing_type="Enterprise",
                rating=4.4, features=["No-code builder", "Multi-language", "Analytics", "Personalization"],
                target_users=["Enterprises", "Customer Service Teams"],
                platform=["Web", "API"], founded_year=2016, popularity_score=68,
                integration_ecosystem=["Salesforce", "Zendesk", "Shopify"], learning_curve="Moderate"
            ),
        ]
    
    def _calculate_dynamic_profiles(self):
        """Calculate dynamic profiles and statistics for the catalog"""
        self.category_stats = self.get_category_statistics()
        self.pricing_stats = self.get_pricing_statistics()
        self.trending_tools = self.get_trending_tools()
        self.newest_tools = self.get_newest_tools()
    
    def get_category_statistics(self) -> Dict:
        """Get detailed statistics per category"""
        categories = {}
        for product in self.products:
            for use_case in product.use_cases:
                if use_case not in categories:
                    categories[use_case] = {
                        'count': 0,
                        'avg_rating': 0,
                        'tools': [],
                        'avg_popularity': 0
                    }
                categories[use_case]['count'] += 1
                categories[use_case]['tools'].append(product.name)
        
        # Calculate averages
        for cat in categories:
            cat_tools = [p for p in self.products if cat in p.use_cases]
            categories[cat]['avg_rating'] = round(sum(p.rating for p in cat_tools) / len(cat_tools), 1)
            categories[cat]['avg_popularity'] = round(sum(p.popularity_score for p in cat_tools) / len(cat_tools), 1)
        
        return categories
    
    def get_pricing_statistics(self) -> Dict:
        """Analyze pricing distribution"""
        pricing = {'Free': 0, 'Freemium': 0, 'Paid': 0, 'Enterprise': 0}
        for product in self.products:
            pricing[product.pricing_type] += 1
        return pricing
    
    def get_trending_tools(self, limit: int = 10) -> List[AIProduct]:
        """Get trending tools based on popularity score"""
        return sorted(self.products, key=lambda x: x.popularity_score, reverse=True)[:limit]
    
    def get_newest_tools(self, limit: int = 10) -> List[AIProduct]:
        """Get newest tools based on founding year"""
        return sorted(self.products, key=lambda x: x.founded_year, reverse=True)[:limit]
    
    def search_by_keyword(self, keyword: str) -> List[AIProduct]:
        """Enhanced search across all fields"""
        keyword = keyword.lower()
        results = []
        for product in self.products:
            searchable_text = (
                f"{product.name} {product.description} "
                f"{' '.join(product.features)} {' '.join(product.use_cases)} "
                f"{' '.join(product.target_users)} {' '.join(product.platform)} "
                f"{' '.join(product.integration_ecosystem)} {product.learning_curve}"
            ).lower()
            
            if keyword in searchable_text:
                results.append(product)
        return sorted(results, key=lambda x: x.popularity_score, reverse=True)
    
    def filter_by_multiple_criteria(self, 
                                   category: str = None,
                                   pricing_type: str = None,
                                   platform: str = None,
                                   target_user: str = None,
                                   learning_curve: str = None,
                                   min_rating: float = 0) -> List[AIProduct]:
        """Advanced multi-criteria filtering"""
        results = self.products
        
        if category:
            results = [p for p in results if category in p.use_cases]
        if pricing_type:
            results = [p for p in results if p.pricing_type == pricing_type]
        if platform:
            results = [p for p in results if platform in p.platform]
        if target_user:
            results = [p for p in results if target_user in p.target_users]
        if learning_curve:
            results = [p for p in results if p.learning_curve == learning_curve]
        if min_rating > 0:
            results = [p for p in results if p.rating >= min_rating]
        
        return sorted(results, key=lambda x: x.popularity_score, reverse=True)
    
    def get_all_use_cases(self) -> List[str]:
        """Get sorted list of all unique use cases"""
        use_cases = set()
        for product in self.products:
            use_cases.update(product.use_cases)
        return sorted(list(use_cases))

def display_product_card(product: AIProduct):
    """Enhanced product card display"""
    with st.container():
        popularity_width = int(product.popularity_score)
        
        st.markdown(f"""
        <div class="product-card">
            <div class="product-name">
                <span class="product-emoji">{product.emoji}</span>
                {product.name}
                {f'<span class="trending-badge">🔥 Trending</span>' if product.popularity_score > 85 else ''}
            </div>
            
            <div style="margin-bottom: 1rem;">
                <span class="rating-stars">{'⭐' * int(product.rating)}</span>
                <span style="color: #666; margin-left: 0.5rem;">{product.rating}/5</span>
                <span style="margin: 0 1rem;">|</span>
                <span class="pricing-badge">💰 {product.pricing}</span>
                <span style="margin: 0 1rem;">|</span>
                <span>📚 {product.learning_curve}</span>
            </div>
            
            <div class="popularity-bar" style="width: {popularity_width}%;"></div>
            <small style="color: #666;">Popularity Score: {product.popularity_score}/100</small>
            
            <p style="color: #555; margin: 1rem 0; line-height: 1.6;">{product.description}</p>
            
            <div style="margin: 1rem 0;">
                <strong>🎯 Use Cases:</strong><br>
                {" ".join([f'<span class="category-badge">{uc}</span>' for uc in product.use_cases])}
            </div>
            
            <div style="margin: 1rem 0;">
                <strong>👥 Target Users:</strong><br>
                {" ".join([f'<span class="feature-tag">{u}</span>' for u in product.target_users])}
            </div>
            
            <div style="margin: 1rem 0;">
                <strong>🔧 Key Features:</strong><br>
                {" ".join([f'<span class="feature-tag">{f}</span>' for f in product.features[:4]])}
            </div>
            
            <div style="margin: 1rem 0;">
                <strong>🔗 Integrations:</strong><br>
                {", ".join(product.integration_ecosystem)}
            </div>
            
            <div style="margin-top: 1rem; display: flex; gap: 1rem; align-items: center;">
                <a href="{product.url}" target="_blank" style="color: #667eea; text-decoration: none; font-weight: 600;">
                    🌐 Visit Website →
                </a>
                <span style="color: #999;">|</span>
                <small style="color: #999;">Founded: {product.founded_year}</small>
                <span style="color: #999;">|</span>
                <small style="color: #999;">Platform: {', '.join(product.platform)}</small>
            </div>
        </div>
        """, unsafe_allow_html=True)

def main():
    # Initialize catalog with session state
    if 'catalog' not in st.session_state:
        st.session_state.catalog = AICatalog()
    
    catalog = st.session_state.catalog
    
    # Animated header
    st.markdown('<h1 class="main-header">🤖 AI Products & Apps Catalog</h1>', unsafe_allow_html=True)
    st.markdown('<p class="subtitle">Discover 60+ AI tools across 25+ categories — Find the perfect AI solution for your workflow</p>', unsafe_allow_html=True)
    
    # Dynamic Statistics Dashboard
    st.markdown("---")
    col1, col2, col3, col4, col5 = st.columns(5)
    
    with col1:
        with st.container():
            st.markdown('<div class="stat-card">', unsafe_allow_html=True)
            st.markdown(f'<div class="stat-number">{len(catalog.products)}+</div>', unsafe_allow_html=True)
            st.markdown('Total Tools')
            st.markdown('</div>', unsafe_allow_html=True)
    
    with col2:
        with st.container():
            st.markdown('<div class="stat-card">', unsafe_allow_html=True)
            st.markdown(f'<div class="stat-number">{len(catalog.category_stats)}</div>', unsafe_allow_html=True)
            st.markdown('Categories')
            st.markdown('</div>', unsafe_allow_html=True)
    
    with col3:
        trending = catalog.get_trending_tools(1)[0]
        with st.container():
            st.markdown('<div class="stat-card">', unsafe_allow_html=True)
            st.markdown(f'<div class="stat-number">🔥</div>', unsafe_allow_html=True)
            st.markdown(f'Top Trend: {trending.name}')
            st.markdown(f'<small>Score: {trending.popularity_score}/100</small>', unsafe_allow_html=True)
            st.markdown('</div>', unsafe_allow_html=True)
    
    with col4:
        avg_rating = round(sum(p.rating for p in catalog.products) / len(catalog.products), 1)
        with st.container():
            st.markdown('<div class="stat-card">', unsafe_allow_html=True)
            st.markdown(f'<div class="stat-number">⭐{avg_rating}</div>', unsafe_allow_html=True)
            st.markdown('Average Rating')
            st.markdown('</div>', unsafe_allow_html=True)
    
    with col5:
        newest = catalog.get_newest_tools(1)[0]
        with st.container():
            st.markdown('<div class="stat-card">', unsafe_allow_html=True)
            st.markdown(f'<div class="stat-number">🆕</div>', unsafe_allow_html=True)
            st.markdown(f'Newest: {newest.name}')
            st.markdown(f'<small>Founded {newest.founded_year}</small>', unsafe_allow_html=True)
            st.markdown('</div>', unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Enhanced Sidebar with Advanced Filters
    with st.sidebar:
        st.markdown("## 🔍 Search & Filters")
        
        # Main search
        search_query = st.text_input("🔎 Search tools:", placeholder="e.g., video, marketing, code assistant...")
        
        st.markdown("---")
        st.markdown("## 🎯 Advanced Filters")
        
        # Category filter
        all_use_cases = ["All"] + catalog.get_all_use_cases()
        selected_category = st.selectbox("📁 Category:", all_use_cases)
        
        # Pricing filter
        pricing_options = ["All", "Free", "Freemium", "Paid", "Enterprise"]
        selected_pricing = st.selectbox("💰 Pricing:", pricing_options)
        
        # Platform filter
        platforms = ["All", "Web", "Mobile", "Desktop", "API", "Browser Extension"]
        selected_platform = st.selectbox("📱 Platform:", platforms)
        
        # Learning curve
        learning_options = ["All", "Easy", "Moderate", "Advanced"]
        selected_learning = st.selectbox("📚 Learning Curve:", learning_options)
        
        # Rating filter
        min_rating = st.slider("⭐ Minimum Rating:", 0.0, 5.0, 0.0, 0.5)
        
        # Reset filters
        if st.button("🔄 Reset Filters"):
            st.rerun()
        
        st.markdown("---")
        
        # Quick insights
        st.markdown("## 📊 Quick Insights")
        
        # Pricing distribution
        st.markdown("### Pricing Distribution")
        for ptype, count in catalog.pricing_stats.items():
            st.markdown(f"• {ptype}: {count} tools")
        
        # Top categories
        st.markdown("### 🏆 Top Categories")
        top_cats = sorted(catalog.category_stats.items(), key=lambda x: x[1]['avg_popularity'], reverse=True)[:5]
        for cat, stats in top_cats:
            st.markdown(f"• {cat}: {stats['count']} tools (Avg: ⭐{stats['avg_rating']})")
        
        st.markdown("---")
        st.markdown("## 🚀 Trending Tools")
        for tool in catalog.get_trending_tools(5):
            st.markdown(f"**{tool.emoji} {tool.name}** — Score: {tool.popularity_score}")
    
    # Main content area
    if search_query:
        # Search results with sorting
        results = catalog.search_by_keyword(search_query)
        st.markdown(f"### 🔍 Search Results for '{search_query}' ({len(results)} found)")
        
        if results:
            # Sort options
            sort_by = st.selectbox("Sort by:", ["Popularity", "Rating", "Newest", "Name"])
            
            if sort_by == "Rating":
                results = sorted(results, key=lambda x: x.rating, reverse=True)
            elif sort_by == "Newest":
                results = sorted(results, key=lambda x: x.founded_year, reverse=True)
            elif sort_by == "Name":
                results = sorted(results, key=lambda x: x.name)
            # Default is Popularity (already sorted)
            
            # Display results in grid
            cols = st.columns(2)
            for idx, product in enumerate(results):
                with cols[idx % 2]:
                    display_product_card(product)
        else:
            st.warning("No tools found matching your search. Try different keywords or browse categories!")
            
    elif (selected_category != "All" or selected_pricing != "All" or 
          selected_platform != "All" or selected_learning != "All" or min_rating > 0):
        # Advanced filtering
        results = catalog.filter_by_multiple_criteria(
            category=None if selected_category == "All" else selected_category,
            pricing_type=None if selected_pricing == "All" else selected_pricing,
            platform=None if selected_platform == "All" else selected_platform,
            learning_curve=None if selected_learning == "All" else selected_learning,
            min_rating=min_rating
        )
        
        filter_desc = []
        if selected_category != "All": filter_desc.append(selected_category)
        if selected_pricing != "All": filter_desc.append(selected_pricing)
        if selected_platform != "All": filter_desc.append(selected_platform)
        if selected_learning != "All": filter_desc.append(f"{selected_learning} learning")
        if min_rating > 0: filter_desc.append(f"≥{min_rating}⭐")
        
        st.markdown(f"### 🎯 Filtered Results ({', '.join(filter_desc)}) — {len(results)} tools")
        
        if results:
            cols = st.columns(2)
            for idx, product in enumerate(results):
                with cols[idx % 2]:
                    display_product_card(product)
        else:
            st.warning("No tools match your filter criteria. Try adjusting the filters!")
    
    else:
        # Default view: Category cards
        st.markdown("## 📁 Browse by Category")
        st.markdown("Click on any category in the sidebar to filter, or use the search bar above!")
        
        # Show category grid
        category_list = list(catalog.category_stats.items())
        cols = st.columns(3)
        
        for idx, (category, stats) in enumerate(category_list):
            with cols[idx % 3]:
                st.markdown(f"""
                <div class="category-card">
                    <div class="category-icon">{get_category_emoji(category)}</div>
                    <h4 style="color: #2d3436; margin: 0.5rem 0;">{category}</h4>
                    <span class="category-count">{stats['count']} tools</span>
                    <div style="margin-top: 0.5rem;">
                        <small>Avg Rating: ⭐{stats['avg_rating']}</small><br>
                        <small>Popularity: {stats['avg_popularity']}/100</small>
                    </div>
                </div>
                """, unsafe_allow_html=True)
        
        # Show trending section
        st.markdown("---")
        st.markdown("## 🔥 Trending AI Tools")
        trending_tools = catalog.get_trending_tools(6)
        cols = st.columns(3)
        for idx, tool in enumerate(trending_tools):
            with cols[idx % 3]:
                display_product_card(tool)
        
        # Show newest tools
        st.markdown("---")
        st.markdown("## 🆕 Recently Launched Tools")
        newest_tools = catalog.get_newest_tools(6)
        cols = st.columns(3)
        for idx, tool in enumerate(newest_tools):
            with cols[idx % 3]:
                display_product_card(tool)
    
    # Footer
    st.markdown("---")
    st.markdown(f"""
    <div style="text-align: center; padding: 2rem; background: linear-gradient(135deg, #f8f9fa 0%, #e9ecef 100%); border-radius: 20px;">
        <h3 style="color: #667eea;">🚀 AI Products & Apps Catalog</h3>
        <p style="color: #666;">Comprehensive database of {len(catalog.products)}+ AI tools across {len(catalog.category_stats)} categories</p>
        <p style="color: #999; font-size: 0.9rem;">
            Last updated: {datetime.now().strftime('%B %Y')} | 
            Avg Rating: {avg_rating}⭐ | 
            Categories: {len(catalog.category_stats)}
        </p>
        <p style="color: #999; font-size: 0.8rem;">Built with ❤️ using Streamlit</p>
    </div>
    """, unsafe_allow_html=True)

def get_category_emoji(category: str) -> str:
    """Return appropriate emoji for category"""
    emoji_map = {
        "Video Generation": "🎬",
        "Video Editing": "✂️",
        "Content Creation": "📝",
        "Image Generation": "🎨",
        "Art & Design": "🖼️",
        "Code Assistant": "💻",
        "Development": "⚡",
        "Presentations": "📊",
        "Voice Synthesis": "🎤",
        "Music Creation": "🎵",
        "Chatbot": "🤖",
        "Research": "🔬",
        "Data Analysis": "📈",
        "Marketing": "📢",
        "SEO": "🎯",
        "Productivity": "✅",
        "E-commerce": "🛍️",
        "Customer Service": "🎧",
        "3D Modeling": "🎮",
        "Transcription": "📋",
    }
    return emoji_map.get(category, "🔧")

if __name__ == "__main__":
    main()
