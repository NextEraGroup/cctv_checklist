
import streamlit as st

st.set_page_config(page_title="CCTV T&C Checklist Generator", layout="wide")

st.title("📋 CCTV T&C Checklist Generator")

project_type = st.selectbox("Select Project Type", [
    "High-rise Building", "Villa/House", "Factory", "Perimeter Surveillance"
])

if st.button("Generate Checklist"):
    st.subheader(f"T&C Checklist for {project_type} Project")
    if project_type == "High-rise Building":
        st.markdown("""
- Verify camera model, lens, and mounting matches shop drawings and specifications
- Check structured cabling continuity and labeling per floor
- Validate NVR/DVR configuration with failover storage setup
- Inspect power supply and UPS backup to each rack location
- Test streaming and recording of live footage from all cameras
- Confirm network IP scheme, VLAN isolation, and switch uplinks
- Ensure integration readiness with BMS/Security Control Room
- Perform day/night testing and record light level adequacy
        """)
    elif project_type == "Villa/House":
        st.markdown("""
- Confirm proper indoor/outdoor camera placement as per layout
- Test camera coverage at all entrance, garage, and perimeter zones
- Verify PoE supply or local adapter connection and protection
- Record quality check on NVR with time/date stamp sync
- User interface setup for mobile viewing or intercom integration
        """)
    elif project_type == "Factory":
        st.markdown("""
- Assess industrial-grade camera enclosure ratings (IP66/IK10)
- Ensure vibration-resistant mounting in high-machine areas
- Inspect fiber connectivity and core switch redundancy
- Validate central command room feeds and event storage
- Confirm integration with factory SCADA or alert systems
        """)
    elif project_type == "Perimeter Surveillance":
        st.markdown("""
- Test IR range and clarity at night for each long-range camera
- Verify fence line detection with PTZ auto-tracking setup
- Check camera pole earthing and surge protection
- Review recording settings for motion-triggered events
- Ensure alert integration with guard control app or siren system
        """)
    st.success("✅ Checklist generated successfully!")
