import time
import winsound
import streamlit as st

st.title("⏱️ Countdown Timer")

timer = st.time_input("⏳ Enter the duration (HH:MM:SS)")
but = st.button("🚀 Start Timer")

if but:
    total_seconds = timer.hour * 3600 + timer.minute * 60 + timer.second
    timer_placeholder = st.empty()
    status_placeholder = st.empty()
    
    status_placeholder.success("⏳ Timer started!")
    
    for i in range(total_seconds, -1, -1):
        mins, secs = divmod(i, 60)
        hours, mins = divmod(mins, 60)
        timer_placeholder.success(f"🕒 {hours:02d}:{mins:02d}:{secs:02d}")
        time.sleep(1)
    
    status_placeholder.empty()
    st.success("⏰ Time's up!")
    st.balloons()
    
    try:
        winsound.Beep(2000, 2000)
    except:
        st.warning("🔊 Sound alert only works on Windows")