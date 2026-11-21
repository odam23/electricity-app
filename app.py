"""Monthly electricity bill split: household 50/50, laundry by hours."""

import streamlit as st

st.set_page_config(page_title="Electricity Bill Split", page_icon="")
st.title("Monthly Electricity Calculator")
#st.write("Household electricity is split **50/50**. Laundry is split by **hours used**.")

# The dryer is 240 V × 26 A = 6,240 W.
# The washer is 120 V × 10 A = 1,200 W.
# Together: (6,240 + 1,200) / 1,000 = 7.44 kW.
with st.form("monthly_bill"):
    st.subheader("Enter this month's numbers")
    total_kwh = st.number_input("Total electricity used (kWh)", min_value=0.01, value=406.0, step=1.0)
    total_bill = st.number_input("Total electricity bill ($)", min_value=0.0, value=155.99, step=1.0)
    power_kw = st.number_input("Washer + dryer combined power (kW)", min_value=0.0, value=7.44, step=0.01)
    col1, col2 = st.columns(2)
    with col1:
        my_hours = st.number_input("Odame's laundry hours", min_value=0.0, value=11.0, step=0.5)
    with col2:
        your_hours = st.number_input("Raphael's laundry hours", min_value=0.0, value=20.0, step=0.5)
    calculate = st.form_submit_button("Calculate our payments", use_container_width=True)

if calculate:
    # 1. Estimate laundry usage in kWh.
    laundry_kwh = power_kw * (my_hours + your_hours)

    if laundry_kwh > total_kwh:
        st.error("Laundry usage is higher than the whole month's usage. Check the hours, power, and total kWh.")
    else:
        # 2. The remaining electricity is household usage, split equally.
        household_kwh = total_kwh - laundry_kwh
        household_bill = total_bill * household_kwh / total_kwh
        household_each = household_bill / 2

        # 3. Laundry cost is split in proportion to hours used.
        laundry_bill = total_bill - household_bill
        total_hours = my_hours + your_hours
        my_laundry_share = my_hours / total_hours if total_hours else 0
        your_laundry_share = your_hours / total_hours if total_hours else 0
        my_laundry_bill = laundry_bill * my_laundry_share
        your_laundry_bill = laundry_bill * your_laundry_share

        # Round the first payment, give the second person the remaining cents.
        my_payment = round(household_each + my_laundry_bill, 2)
        your_payment = round(total_bill - my_payment, 2)
        my_pct = (household_kwh / 2 + power_kw * my_hours) / total_kwh * 100
        your_pct = 100 - my_pct

        st.success("Monthly calculation complete")
        st.subheader("1. Electricity usage")
        st.write(f"**Laundry:** {laundry_kwh:.2f} kWh")
        st.write(f"**Remaining household:** {total_kwh:.2f} − {laundry_kwh:.2f} = **{household_kwh:.2f} kWh**")

        st.subheader("2. Household bill — 50/50")
        st.write(f"Household portion: **${household_bill:.2f}**")
        st.write(f"Each person gets half: **${household_each:.2f}**")

        st.subheader("3. Laundry bill — based on hours")
        st.write(f"Laundry portion: **${laundry_bill:.2f}**")
        st.write(f"**Me:** {my_hours:g} of {total_hours:g} hours = **{my_laundry_share * 100:.2f}%** of laundry (${my_laundry_bill:.2f})")
        st.write(f"**You:** {your_hours:g} of {total_hours:g} hours = **{your_laundry_share * 100:.2f}%** of laundry (${your_laundry_bill:.2f})")

        st.subheader("4. Final payment")
        left, right = st.columns(2)
        with left:
            st.metric("Me", f"${my_payment:.2f}")
            st.caption(f"{my_pct:.2f}% of the total bill")
        with right:
            st.metric("You", f"${your_payment:.2f}")
            st.caption(f"{your_pct:.2f}% of the total bill")
        st.info(f"Both payments add up to **${my_payment + your_payment:.2f}**.")

# st.caption("Estimate only: assumes both machines draw their stated combined power for all recorded laundry hours.")
