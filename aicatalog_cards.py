"""
streamlit_app.py - AI Products Catalog for Streamlit Deployment
Save this file in your GitHub repository
"""

import streamlit as st
import pandas as pd
from typing import List, Dict
from dataclasses import dataclass

# Page configuration
st.set_page_config(
    page_title="AI Products Catalog",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
    <style>
    .main-header {
        font-size: 3rem;
        text-align: center;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 2rem;
    }
    .product-card {
        background: white;
        padding: 1.5rem;
        border-radius: 15px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        margin-bottom: 1rem;
        border-left: 5px solid #667eea;
    }
    .product-name {
        color: #667eea;
        font-size: 1.3rem;
        font-weight: bold;
        margin-bottom: 0.5rem;
    }
    .category-badge {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 0.2rem 0.8rem;
        border-radius: 20px;
        font-size: 0.8rem;
        display: inline-block;
        margin: 0.2rem;
    }
    .rating-stars {
        color: #ffd700;
        font-size: 1.2rem;
    }
    .pricing-badge {
        background: #f0f2f6;
        padding: 0.3rem 0.8rem;
        border-radius: 10px;
        font-size: 0.9rem;
        color: #333;
    }
    .feature-tag {
        background: #e8eaf6;
        color: #667eea;
        padding: 0.2rem 0.6rem;
        border-radius: 15px;
        font-size: 0.8rem;
        display: inline-block;
        margin: 0.2rem;
    }
    </style>
""", unsafe_allow_html=True)

@dataclass
class AIProduct:
    name: str
    url: str
    description: str
    use_cases: List[str]
    pricing: str
    rating: float
    features: List[str]

class AICatalog:
    def __init__(self):
        self.products = self._initialize_catalog()
    
    def _initialize_catalog(self):
        return [
            AIProduct(
                name="Runway ML",
                url="https://runwayml.com",
                description="AI-powered creative tools for video editing, generation, and visual effects",
                use_cases=["Video Generation", "Video Editing", "Image Generation"],
                pricing="Free / Pro from $12/mo",
                rating=4.5,
                features=["Text-to-video", "Green screen", "Motion tracking", "Image generation"]
            ),
            AIProduct(
                name="Synthesia",
                url="https://synthesia.io",
                description="Create AI videos with virtual presenters from text",
                use_cases=["Video Generation", "Presentation Creation"],
                pricing="From $30/mo",
                rating=4.7,
                features=["AI avatars", "120+ languages", "Custom backgrounds", "Script to video"]
            ),
            AIProduct(
                name="Jasper",
                url="https://jasper.ai",
                description="AI content platform for marketing teams",
                use_cases=["Text Generation", "Script Writing", "Social Media Management"],
                pricing="From $49/mo",
                rating=4.6,
                features=["Blog posts", "Social media", "Ad copy", "Brand voice"]
            ),
            AIProduct(
                name="Beautiful.ai",
                url="https://beautiful.ai",
                description="AI-powered presentation software",
                use_cases=["Presentation Creation", "Design Tools"],
                pricing="Free / Pro from $12/mo",
                rating=4.4,
                features=["Smart templates", "Auto-layout", "Collaboration", "Brand control"]
            ),
            AIProduct(
                name="Midjourney",
                url="https://midjourney.com",
                description="AI image generation through Discord",
                use_cases=["Image Generation", "Design Tools"],
                pricing="From $10/mo",
                rating=4.8,
                features=["Text-to-image", "Style variation", "High resolution", "Creative control"]
            ),
            AIProduct(
                name="GitHub Copilot",
                url="https://github.com/features/copilot",
                description="AI pair programmer for code completion",
                use_cases=["Code Assistant"],
                pricing="$10/mo",
                rating=4.7,
                features=["Code completion", "Multiple languages", "IDE integration", "Context awareness"]
            ),
            AIProduct(
                name="Descript",
                url="https://descript.com",
                description="All-in-one video and audio editing with AI",
                use_cases=["Video Editing", "Voice Synthesis"],
                pricing="Free / Pro from $24/mo",
                rating=4.6,
                features=["Text-based editing", "Screen recording", "AI voices", "Transcription"]
            ),
            AIProduct(
                name="ChatGPT",
                url="https://chat.openai.com",
                description="OpenAI's conversational AI assistant",
                use_cases=["Text Generation", "Chatbot", "Code Assistant", "Research"],
                pricing="Free / Plus $20/mo",
                rating=4.8,
                features=["Conversational AI", "Code generation", "Research", "Multilingual"]
            ),
            AIProduct(
                name="DALL-E 3",
                url="https://openai.com/dall-e-3",
                description="Advanced AI image generation by OpenAI",
                use_cases=["Image Generation", "Design Tools"],
                pricing="Pay per image / ChatGPT Plus",
                rating=4.7,
                features=["Text-to-image", "High accuracy", "Style control", "Safe filters"]
            ),
            AIProduct(
                name="Murf.ai",
                url="https://murf.ai",
                description="AI voice generator for realistic voiceovers",
                use_cases=["Voice Synthesis", "Video Generation"],
                pricing="Free / Pro from $19/mo",
                rating=4.4,
                features=["120+ voices", "20+ languages", "Voice cloning", "Background music"]
            ),
            AIProduct(
                name="Canva AI",
                url="https://canva.com",
                description="Design platform with integrated AI features",
                use_cases=["Design Tools", "Presentation Creation", "Social Media"],
                pricing="Free / Pro from $12.99/mo",
                rating=4.7,
                features=["AI design", "Magic resize", "Text-to-image", "Brand templates"]
            ),
            AIProduct(
                name="Copy.ai",
                url="https://copy.ai",
                description="AI copywriting tool for marketing content",
                use_cases=["Text Generation", "Script Writing", "SEO Optimization"],
                pricing="Free / Pro from $49/mo",
                rating=4.5,
                features=["Blog writer", "Social captions", "Email copy", "Product descriptions"]
            ),
        ]
    
    def search_by_keyword(self, keyword: str) -> List[AIProduct]:
        keyword = keyword.lower()
        results = []
        for product in self.products:
            searchable_text = f"{product.name} {product.description} {' '.join(product.features)} {' '.join(product.use_cases)}".lower()
            if keyword in searchable_text:
                results.append(product)
        return results
    
    def get_categories(self) -> Dict[str, List[AIProduct]]:
        categories = {}
        for product in self.products:
            for use_case in product.use_cases:
                if use_case not in categories:
                    categories[use_case] = []
                categories[use_case].append(product)
        return dict(sorted(categories.items()))

def display_product_card(product: AIProduct):
    """Display a single product in a styled card"""
    with st.container():
        st.markdown(f"""
        <div class="product-card">
            <div class="product-name">{product.name}</div>
            <div style="margin-bottom: 0.5rem;">
                <span class="rating-stars">{'⭐' * int(product.rating)}</span>
                <span style="color: #666; margin-left: 0.5rem;">{product.rating}/5</span>
                <span class="pricing-badge" style="margin-left: 1rem;">💰 {product.pricing}</span>
            </div>
            <p style="color: #555; margin: 0.5rem 0;">{product.description}</p>
            <div style="margin: 0.5rem 0;">
                <strong>Use Cases:</strong><br>
                {" ".join([f'<span class="category-badge">{uc}</span>' for uc in product.use_cases])}
            </div>
            <div style="margin: 0.5rem 0;">
                <strong>Key Features:</strong><br>
                {" ".join([f'<span class="feature-tag">{f}</span>' for f in product.features[:4]])}
            </div>
            <a href="{product.url}" target="_blank" style="color: #667eea; text-decoration: none; font-weight: bold;">
                🔗 Visit Website →
            </a>
        </div>
        """, unsafe_allow_html=True)

def main():
    # Initialize catalog
    if 'catalog' not in st.session_state:
        st.session_state.catalog = AICatalog()
    
    catalog = st.session_state.catalog
    
    # Header
    st.markdown('<h1 class="main-header">🤖 AI Products & Apps Catalog</h1>', unsafe_allow_html=True)
    st.markdown("### Discover the perfect AI tools for your specific needs")
    
    # Sidebar
    with st.sidebar:
        st.markdown("## 🔍 Search & Filter")
        
        # Search box
        search_query = st.text_input("Search by keyword:", placeholder="e.g., video, text, code...")
        
        st.markdown("---")
        st.markdown("## 📁 Categories")
        
        # Category filter
        categories = catalog.get_categories()
        selected_category = st.selectbox(
            "Filter by category:",
            ["All Categories"] + list(categories.keys())
        )
        
        st.markdown("---")
        st.markdown("## 📊 Stats")
        st.metric("Total Tools", len(catalog.products))
        st.metric("Categories", len(categories))
        
        # Show category distribution
        st.markdown("### Tools per Category")
        for cat, products in categories.items():
            st.markdown(f"• {cat}: {len(products)}")
    
    # Main content area
    if search_query:
        # Display search results
        results = catalog.search_by_keyword(search_query)
        st.markdown(f"### 🔍 Search Results for '{search_query}' ({len(results)} found)")
        
        if results:
            # Create columns for grid layout
            cols = st.columns(2)
            for idx, product in enumerate(results):
                with cols[idx % 2]:
                    display_product_card(product)
        else:
            st.warning("No products found matching your search. Try different keywords!")
    
    elif selected_category != "All Categories":
        # Display category results
        category_products = categories[selected_category]
        st.markdown(f"### 📁 {selected_category} ({len(category_products)} tools)")
        
        cols = st.columns(2)
        for idx, product in enumerate(category_products):
            with cols[idx % 2]:
                display_product_card(product)
    
    else:
        # Display category boxes (default view)
        st.markdown("### 📁 Browse by Category")
        
        # Create category cards in a grid
        cols = st.columns(3)
        for idx, (category, products) in enumerate(categories.items()):
            with cols[idx % 3]:
                with st.container():
                    st.markdown(f"""
                    <div style="
                        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                        padding: 1.5rem;
                        border-radius: 15px;
                        color: white;
                        margin-bottom: 1rem;
                        cursor: pointer;
                        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
                    ">
                        <h4 style="color: white; margin: 0;">{category}</h4>
                        <p style="margin: 0.5rem 0 0 0; opacity: 0.9;">{len(products)} tools available</p>
                    </div>
                    """, unsafe_allow_html=True)
                    
                    # Show top 3 products in each category
                    for product in products[:3]:
                        st.markdown(f"• **{product.name}** ⭐{product.rating}")
    
    # Footer
    st.markdown("---")
    st.markdown("""
    <div style="text-align: center; color: #666; padding: 2rem;">
        <p>🚀 AI Products Catalog - Helping you find the right AI tools for your workflow</p>
        <p>Built with ❤️ using Streamlit</p>
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
