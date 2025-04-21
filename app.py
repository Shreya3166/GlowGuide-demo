import streamlit as st

st.set_page_config(page_title="GlowGuide - AI Beauty Companion", layout="centered")
st.title("💄 GlowGuide - Your AI Beauty Companion (Demo)")
st.markdown("""
Welcome to **GlowGuide**!  
This is a demo version of our AI-powered assistant that helps you find the best skincare and makeup products based on your skin type, problems, and budget.
""")

# User input
name = st.text_input("👤 Enter Your Name")

if name:
    st.markdown(f"### 👋 Welcome to GlowGuide, **{name}**!")

    skin_type = st.selectbox("💧 Select your skin type", ["Oily", "Dry", "Combination", "Normal", "Sensitive"])
    skin_problems = st.multiselect("❗ Select your skin concerns", ["Acne", "Dark Spots", "Pigmentation", "Tanning", "Wrinkles", "Dullness"])
    budget = st.slider("💸 Your monthly skincare budget (in ₹)", 100, 5000, step=100)

    # Profile Summary
    st.markdown("---")
    st.subheader("✨ Your Profile Summary")
    st.info(f"""
- **Name**: {name}  
- **Skin Type**: {skin_type}  
- **Problems**: {', '.join(skin_problems)}  
- **Budget**: ₹{budget}
""")

    # Product database
    products = [
        {"name": "Salicylic Acid Face Wash", "type": "Oily", "problems": ["Acne"], "price": 250},
        {"name": "Tea Tree Toner", "type": "Oily", "problems": ["Acne", "Dullness"], "price": 180},
        {"name": "Vitamin C Serum", "type": "All", "problems": ["Pigmentation", "Dark Spots"], "price": 500},
        {"name": "Niacinamide Serum", "type": "All", "problems": ["Dark Spots", "Wrinkles"], "price": 450},
        {"name": "Aloe Vera Gel", "type": "Dry", "problems": ["Dullness"], "price": 150},
        {"name": "Hyaluronic Acid Moisturizer", "type": "Dry", "problems": ["Wrinkles", "Dullness"], "price": 550},
        {"name": "Cucumber Toner", "type": "Combination", "problems": ["Tanning"], "price": 120},
        {"name": "Charcoal Face Wash", "type": "Combination", "problems": ["Acne", "Dullness"], "price": 230},
        {"name": "Sunscreen SPF 50", "type": "All", "problems": ["Tanning"], "price": 400},
        {"name": "Retinol Cream", "type": "Sensitive", "problems": ["Wrinkles"], "price": 700},
        {"name": "Gentle Foaming Cleanser", "type": "Sensitive", "problems": ["Dark Spots", "Dullness"], "price": 320},
        {"name": "Rose Water Mist", "type": "Normal", "problems": ["Dullness", "Tanning"], "price": 200}
    ]

    # Recommendation Logic
    recommended = []
    for product in products:
        if (
            (product["type"].lower() == skin_type.lower() or product["type"] == "All")
            and any(problem in product["problems"] for problem in skin_problems)
            and product["price"] <= budget
        ):
            recommended.append(product)

    # Output
    st.markdown("---")
    st.subheader("🧴 Recommended Products for You")

    if recommended:
        for product in recommended:
            st.success(f"""
**{product['name']}**  
💰 Price: ₹{product['price']}  
🎯 Targets: {', '.join(product['problems'])}
            """)
            st.markdown("---")
    else:
        st.warning("😢 No products match your preferences. Try increasing your budget or changing your selections.")

    st.markdown("---")
    st.caption("🔬 This is a demo version of GlowGuide AI. All products are sample-based for demo purposes only.")

