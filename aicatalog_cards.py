"""
streamlit_app.py - AI Products & Apps Catalog (Fixed Rendering)
Uses Streamlit native components with minimal HTML for decoration only
"""

import streamlit as st
from typing import List, Dict
from dataclasses import dataclass
from datetime import datetime

# Page configuration
st.set_page_config(
    page_title="AI Products & Apps Catalog",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Minimal CSS - only for accents and decorations that won't break
st.markdown("""
    <style>
    /* Just a few safe styles */
    .stat-number {
        font-size: 2rem;
        font-weight: bold;
        color: #667eea;
    }
    .footer-text {
        text-align: center;
        color: #666;
        padding: 2rem;
    }
    </style>
""", unsafe_allow_html=True)

@dataclass
class AIProduct:
    """AI Product data model"""
    name: str
    emoji: str
    url: str
    description: str
    use_cases: List[str]
    pricing: str
    pricing_type: str
    rating: float
    features: List[str]
    target_users: List[str]
    platform: List[str]
    founded_year: int
    popularity_score: float
    integration_ecosystem: List[str]
    learning_curve: str

class AICatalog:
    """Extended catalog with AI tools"""
    
    def __init__(self):
        self.products = self._initialize_catalog()
        self._calculate_stats()
    
    def _initialize_catalog(self) -> List[AIProduct]:
        """Initialize catalog with AI tools"""
        
        return [
            # VIDEO GENERATION & EDITING
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
            
            # TEXT & CONTENT GENERATION
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
            
            # IMAGE GENERATION
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
            AIProduct(
                name="Canva AI", emoji="🎨",
                url="https://canva.com",
                description="All-in-one design platform with integrated AI features",
                use_cases=["Design", "Presentations", "Social Media", "Image Generation"],
                pricing="Free / $12.99/mo", pricing_type="Freemium",
                rating=4.7, features=["Magic design", "Text-to-image", "Background remover", "Brand kit"],
                target_users=["Designers", "Marketers", "Everyone"],
                platform=["Web", "Mobile"], founded_year=2013, popularity_score=95,
                integration_ecosystem=["Dropbox", "Google Drive", "Instagram"], learning_curve="Easy"
            ),
            
            # CODE & DEVELOPMENT
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
            
            # CHATBOTS & AI ASSISTANTS
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
            
            # VOICE & AUDIO
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
            
            # MUSIC GENERATION
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
            
            # PRODUCTIVITY
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
            
            # PRESENTATION
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
            
            # MARKETING & SEO
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
            
            # MEETING & TRANSCRIPTION
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
            
            # 3D MODELING
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
            
            # E-COMMERCE
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
            
            # CUSTOMER SERVICE
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
        ]
    
    def _calculate_stats(self):
        """Calculate dynamic statistics"""
        self.category_stats = {}
        for product in self.products:
            for use_case in product.use_cases:
                if use_case not in self.category_stats:
                    self.category_stats[use_case] = {'count': 0, 'total_rating': 0, 'total_popularity': 0}
                self.category_stats[use_case]['count'] += 1
                self.category_stats[use_case]['total_rating'] += product.rating
                self.category_stats[use_case]['total_popularity'] += product.popularity_score
        
        for cat in self.category_stats:
            count = self.category_stats[cat]['count']
            self.category_stats[cat]['avg_rating'] = round(self.category_stats[cat]['total_rating'] / count, 1)
            self.category_stats[cat]['avg_popularity'] = round(self.category_stats[cat]['total_popularity'] / count, 1)
        
        self.pricing_stats = {'Free': 0, 'Freemium': 0, 'Paid': 0, 'Enterprise': 0}
        for product in self.products:
            self.pricing_stats[product.pricing_type] += 1
    
    def search_by_keyword(self, keyword: str) -> List[AIProduct]:
        """Search across all fields"""
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
                                   learning_curve: str = None,
                                   min_rating: float = 0) -> List[AIProduct]:
        """Multi-criteria filtering"""
        results = self.products
        if category:
            results = [p for p in results if category in p.use_cases]
        if pricing_type:
            results = [p for p in results if p.pricing_type == pricing_type]
        if platform:
            results = [p for p in results if platform in p.platform]
        if learning_curve:
            results = [p for p in results if p.learning_curve == learning_curve]
        if min_rating > 0:
            results = [p for p in results if p.rating >= min_rating]
        return sorted(results, key=lambda x: x.popularity_score, reverse=True)
    
    def get_all_use_cases(self) -> List[str]:
        """Get sorted unique use cases"""
        use_cases = set()
        for product in self.products:
            use_cases.update(product.use_cases)
        return sorted(list(use_cases))

def display_product_card(product: AIProduct):
    """Display product card using Streamlit native components"""
    
    # Use expander for clean card-like appearance
    with st.expander(f"{product.emoji} **{product.name}** — {'⭐' * int(product.rating)} {product.rating}/5", expanded=False):
        
        # Two columns for layout
        col1, col2 = st.columns([2, 1])
        
        with col1:
            st.markdown(f"**Description:** {product.description}")
            
            # Use cases
            st.markdown("**🎯 Use Cases:**")
            st.markdown("  \n".join([f"• {uc}" for uc in product.use_cases]))
            
            # Features
            st.markdown("**🔧 Key Features:**")
            st.markdown("  \n".join([f"• {f}" for f in product.features]))
        
        with col2:
            # Pricing
            if product.pricing_type == "Freemium":
                st.success(f"💰 {product.pricing}")
            elif product.pricing_type == "Free":
                st.info(f"🆓 {product.pricing}")
            else:
                st.warning(f"💳 {product.pricing}")
            
            # Rating
            st.metric("Rating", f"{'⭐' * int(product.rating)} {product.rating}/5")
            
            # Popularity
            st.metric("Popularity", f"{product.popularity_score}/100")
            
            # Learning curve
            curve_color = "🟢" if product.learning_curve == "Easy" else "🟡" if product.learning_curve == "Moderate" else "🔴"
            st.markdown(f"**Learning Curve:** {curve_color} {product.learning_curve}")
            
            # Founded
            st.markdown(f"**Founded:** {product.founded_year}")
            
            # Platform
            st.markdown(f"**Platform:** {', '.join(product.platform)}")
        
        # Target users
        st.markdown("**👥 Target Users:** " + " | ".join(product.target_users))
        
        # Integrations
        st.markdown("**🔗 Integrations:** " + " | ".join(product.integration_ecosystem))
        
        # Visit website button
        st.link_button(f"🌐 Visit {product.name}", product.url)

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
        "Marketing": "📢",
        "SEO": "🎯",
        "Productivity": "✅",
        "E-commerce": "🛍️",
        "Customer Service": "🎧",
        "3D Modeling": "🎮",
        "Transcription": "📋",
        "Design": "🎨",
        "Social Media": "📱",
        "Copywriting": "✍️",
        "E-Learning": "📚",
        "Podcasting": "🎙️",
        "Gaming": "🎮",
        "Documentation": "📄",
        "Project Management": "📊",
        "Meeting Assistant": "🤝",
    }
    return emoji_map.get(category, "🔧")

def main():
    # Initialize catalog
    if 'catalog' not in st.session_state:
        st.session_state.catalog = AICatalog()
    
    catalog = st.session_state.catalog
    
    # Header
    st.title("🤖 AI Products & Apps Catalog")
    st.markdown("*Discover 35+ AI tools across 25+ categories — Find the perfect AI solution for your workflow*")
    
    # Statistics Dashboard
    st.divider()
    
    avg_rating = round(sum(p.rating for p in catalog.products) / len(catalog.products), 1)
    
    col1, col2, col3, col4, col5 = st.columns(5)
    
    with col1:
        st.metric("Total Tools", f"{len(catalog.products)}+")
    
    with col2:
        st.metric("Categories", len(catalog.category_stats))
    
    with col3:
        trending = sorted(catalog.products, key=lambda x: x.popularity_score, reverse=True)[0]
        st.metric("🔥 Top Tool", trending.name)
    
    with col4:
        st.metric("Avg Rating", f"⭐ {avg_rating}")
    
    with col5:
        newest = sorted(catalog.products, key=lambda x: x.founded_year, reverse=True)[0]
        st.metric("🆕 Newest", newest.name)
    
    st.divider()
    
    # Sidebar
    with st.sidebar:
        st.header("🔍 Search & Filters")
        
        search_query = st.text_input("Search tools:", placeholder="e.g., video, marketing, code...")
        
        st.divider()
        st.subheader("🎯 Advanced Filters")
        
        all_use_cases = ["All"] + catalog.get_all_use_cases()
        selected_category = st.selectbox("Category:", all_use_cases)
        
        pricing_options = ["All", "Free", "Freemium", "Paid", "Enterprise"]
        selected_pricing = st.selectbox("Pricing:", pricing_options)
        
        platforms = ["All", "Web", "Mobile", "Desktop", "API", "Browser Extension"]
        selected_platform = st.selectbox("Platform:", platforms)
        
        learning_options = ["All", "Easy", "Moderate", "Advanced"]
        selected_learning = st.selectbox("Learning Curve:", learning_options)
        
        min_rating = st.slider("Minimum Rating:", 0.0, 5.0, 0.0, 0.5)
        
        if st.button("🔄 Reset Filters", use_container_width=True):
            st.rerun()
        
        st.divider()
        
        # Stats in sidebar
        st.subheader("💰 Pricing Distribution")
        for ptype, count in catalog.pricing_stats.items():
            st.write(f"• **{ptype}**: {count} tools")
        
        st.divider()
        
        st.subheader("🏆 Top Categories")
        top_cats = sorted(catalog.category_stats.items(), 
                         key=lambda x: x[1]['avg_popularity'], 
                         reverse=True)[:5]
        for cat, stats in top_cats:
            st.write(f"• **{cat}**: {stats['count']} tools (⭐{stats['avg_rating']})")
    
    # Main content area
    if search_query:
        results = catalog.search_by_keyword(search_query)
        st.subheader(f"🔍 Search Results for '{search_query}' ({len(results)} found)")
        
        if results:
            sort_by = st.selectbox("Sort by:", ["Popularity", "Rating", "Newest", "Name"], key="sort_search")
            
            if sort_by == "Rating":
                results = sorted(results, key=lambda x: x.rating, reverse=True)
            elif sort_by == "Newest":
                results = sorted(results, key=lambda x: x.founded_year, reverse=True)
            elif sort_by == "Name":
                results = sorted(results, key=lambda x: x.name)
            
            for product in results:
                display_product_card(product)
        else:
            st.warning("No tools found. Try different keywords!")
    
    elif (selected_category != "All" or selected_pricing != "All" or 
          selected_platform != "All" or selected_learning != "All" or min_rating > 0):
        
        results = catalog.filter_by_multiple_criteria(
            category=None if selected_category == "All" else selected_category,
            pricing_type=None if selected_pricing == "All" else selected_pricing,
            platform=None if selected_platform == "All" else selected_platform,
            learning_curve=None if selected_learning == "All" else selected_learning,
            min_rating=min_rating
        )
        
        filters = []
        if selected_category != "All": filters.append(selected_category)
        if selected_pricing != "All": filters.append(selected_pricing)
        if selected_platform != "All": filters.append(selected_platform)
        
        st.subheader(f"🎯 Filtered Results ({', '.join(filters) if filters else 'All'}) — {len(results)} tools")
        
        if results:
            for product in results:
                display_product_card(product)
        else:
            st.warning("No tools match your criteria. Try adjusting filters!")
    
    else:
        # Default view: Category grid
        st.subheader("📁 Browse by Category")
        st.caption("Select a category from the sidebar or use the search bar to find tools")
        
        # Display category cards in a grid
        category_list = list(catalog.category_stats.items())
        
        # Create rows of 3 columns
        for i in range(0, len(category_list), 3):
            cols = st.columns(3)
            for j in range(3):
                if i + j < len(category_list):
                    category, stats = category_list[i + j]
                    with cols[j]:
                        with st.container(border=True):
                            st.markdown(f"### {get_category_emoji(category)}")
                            st.markdown(f"**{category}**")
                            st.write(f"📦 {stats['count']} tools")
                            st.write(f"⭐ {stats['avg_rating']} avg rating")
                            st.write(f"📊 {stats['avg_popularity']}/100 popularity")
        
        st.divider()
        
        # Trending section
        st.subheader("🔥 Trending AI Tools")
        trending_tools = sorted(catalog.products, key=lambda x: x.popularity_score, reverse=True)[:6]
        
        for i in range(0, len(trending_tools), 2):
            cols = st.columns(2)
            for j in range(2):
                if i + j < len(trending_tools):
                    with cols[j]:
                        display_product_card(trending_tools[i + j])
    
    # Footer
    st.divider()
    st.markdown(f"""
    <div class="footer-text">
        <h3>🚀 AI Products & Apps Catalog</h3>
        <p>Comprehensive database of {len(catalog.products)}+ AI tools across {len(catalog.category_stats)} categories</p>
        <p>Last updated: {datetime.now().strftime('%B %Y')} | Avg Rating: {avg_rating}⭐ | Categories: {len(catalog.category_stats)}</p>
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
