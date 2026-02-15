import streamlit as st

# ==========================================================
# PAGE CONFIG
# ==========================================================

st.set_page_config(page_title="Elite Performance Engine", layout="wide")
st.title("🔥 Elite Performance Engine")
st.write("Structured. Calculated. Personalized.")

# ==========================================================
# ATHLETE PROFILE
# ==========================================================

st.header("📋 Athlete Profile Assessment")

col1, col2 = st.columns(2)

with col1:
    age = st.number_input("Age", 15, 60, 18)
    weight = st.number_input("Weight (kg)", 40, 150, 70)
    height = st.number_input("Height (cm)", 140, 210, 170)
    bodyfat = st.slider("Estimated Body Fat %", 5, 40, 15)

with col2:
    goal = st.selectbox(
        "Primary Goal",
        ["Build Muscle", "Lose Fat", "Athletic Performance"]
    )

    experience = st.selectbox(
        "Training Experience",
        ["Beginner", "Intermediate", "Advanced"]
    )

    training_days = st.slider("Training Days per Week", 3, 6, 4)
    activity_level = st.selectbox(
        "Daily Activity Level",
        ["Sedentary", "Moderate", "Very Active"]
    )

generate = st.button("Generate Full Performance Blueprint")

# ==========================================================
# CALORIE ENGINE
# ==========================================================

def calculate_tdee(weight, height, age, activity):
    bmr = (10 * weight) + (6.25 * height) - (5 * age) + 5
    
    multiplier = {
        "Sedentary": 1.4,
        "Moderate": 1.6,
        "Very Active": 1.8
    }

    return bmr * multiplier[activity]

# ==========================================================
# TRAINING ENGINE
# ==========================================================

def generate_training(goal, experience, days):
    st.header("🏋️ Structured Weekly Training Blueprint")

    st.markdown("### Weekly Structure")

    if goal == "Build Muscle":
        split = ["Push", "Pull", "Legs"]
    elif goal == "Lose Fat":
        split = ["Upper Strength", "Lower Strength", "Conditioning"]
    else:
        split = ["Strength", "Explosive Power", "Conditioning"]

    for day in range(days):
        st.subheader(f"Day {day+1} – {split[day % len(split)]}")

        st.write("1️⃣ Primary Compound Lift (Heavy Strength Focus)")
        st.write("   - 4–5 sets")
        st.write("   - 4–8 reps")
        st.write("   - 2–3 min rest")

        st.write("2️⃣ Secondary Compound Movement")
        st.write("   - 3–4 sets")
        st.write("   - 6–10 reps")

        st.write("3️⃣ Accessory Isolation Work")
        st.write("   - 3 sets")
        st.write("   - 10–15 reps")

        st.write("4️⃣ Core / Stability Training")
        st.write("   - Planks, anti-rotation work")

        if goal == "Athletic Performance":
            st.write("5️⃣ Explosive Finisher")
            st.write("   - Sprints / Jumps / Med Ball Throws")

        st.write("")

    st.markdown("### 📈 Progressive Overload Strategy")
    st.write("• Increase load 2–5% weekly if reps are achieved.")
    st.write("• Deload every 6–8 weeks.")
    st.write("• Track strength progression.")

# ==========================================================
# NUTRITION ENGINE
# ==========================================================

def generate_nutrition(goal, tdee, weight):
    st.header("🥗 Personalized Nutrition Strategy")

    if goal == "Build Muscle":
        calories = tdee + 400
    elif goal == "Lose Fat":
        calories = tdee - 400
    else:
        calories = tdee

    protein = weight * 2
    fats = (calories * 0.25) / 9
    carbs = (calories - (protein * 4 + fats * 9)) / 4

    st.markdown("### 🔥 Daily Energy Target")
    st.success(f"{int(calories)} kcal/day")

    st.markdown("### ⚖ Macronutrient Breakdown")
    st.write(f"Protein: {int(protein)} g (Muscle repair & recovery)")
    st.write(f"Fats: {int(fats)} g (Hormone health)")
    st.write(f"Carbohydrates: {int(carbs)} g (Training fuel)")

    st.markdown("### 🥦 Nutrient Timing Strategy")
    st.write("• Consume carbs pre & post workout.")
    st.write("• Protein every 3–4 hours.")
    st.write("• Hydrate before, during, after training.")

    st.markdown("### 🍽 Whole Food Recommendations")
    st.write("Lean proteins: Eggs, chicken, fish, lentils")
    st.write("Complex carbs: Rice, oats, potatoes")
    st.write("Healthy fats: Nuts, seeds, olive oil")

# ==========================================================
# MICRONUTRIENT SYSTEM
# ==========================================================

def show_micronutrients():
    st.header("🧬 Complete Micronutrient Optimization")

    st.markdown("### 🟢 Essential Vitamins")
    st.write("Vitamin A – Vision & immunity – Carrots, spinach")
    st.write("Vitamin B Complex – Energy metabolism – Whole grains, meat")
    st.write("Vitamin C – Collagen & recovery – Citrus fruits")
    st.write("Vitamin D – Hormonal balance – Sunlight")
    st.write("Vitamin E – Antioxidant – Nuts")
    st.write("Vitamin K – Bone metabolism – Leafy greens")

    st.markdown("### 🔵 Essential Minerals")
    st.write("Calcium – Bone strength – Dairy")
    st.write("Magnesium – Muscle recovery – Nuts")
    st.write("Iron – Oxygen transport – Red meat")
    st.write("Zinc – Testosterone support – Seeds")
    st.write("Selenium – Thyroid support – Brazil nuts")
    st.write("Iodine – Thyroid hormones – Iodized salt")
    st.write("Chromium – Blood sugar regulation – Broccoli")
    st.write("Molybdenum – Enzyme activation – Legumes")
    st.write("Cobalt – Part of Vitamin B12 – Animal foods")

# ==========================================================
# RECOVERY ENGINE
# ==========================================================

def show_recovery():
    st.header("🛌 Recovery & Longevity Strategy")

    st.write("• Sleep 7–9 hours consistently.")
    st.write("• 1–2 full rest days weekly.")
    st.write("• Mobility training 2–3x weekly.")
    st.write("• Manage stress & avoid overtraining.")
    st.write("• Monitor fatigue markers.")

# ==========================================================
# MAIN EXECUTION
# ==========================================================

if generate:
    tdee = calculate_tdee(weight, height, age, activity_level)

    generate_training(goal, experience, training_days)
    st.divider()

    generate_nutrition(goal, tdee, weight)
    st.divider()

    show_micronutrients()
    st.divider()

    show_recovery()
