import streamlit as st
import random

def main():
    """A CSS Shape Generator App by Amna"""
    st.title("Advanced CSS Shape Generator by Amna")

    activity = ['Design', 'About']
    choice = st.sidebar.selectbox("Select Activity", activity)

    if choice == 'Design':
        st.subheader("Design Your Shape")
        
        # Basic color pickers
        col1, col2 = st.columns(2)
        with col1:
            bgcolor = st.color_picker("Pick Background color", "#0000FF")
        with col2:
            fontcolor = st.color_picker("Pick Font Color", "#FFFFFF")

        # Display header with selected colors
        html_temp = """
        <div style="background-color:{};padding:10px;border-radius:10px">
        <h1 style="color:{};text-align:center;">CSS Shape Generator by Amna</h1>
        </div>
        """
        st.markdown(html_temp.format(bgcolor, fontcolor), unsafe_allow_html=True)

        # ADVANCED FEATURE 1: Gradient Background Option
        st.subheader("Advanced Options")
        use_gradient = st.checkbox("Use Gradient Background")
        
        if use_gradient:
            col1, col2 = st.columns(2)
            with col1:
                gradient_color1 = st.color_picker("Gradient Color 1", "#FF0000")
            with col2:
                gradient_color2 = st.color_picker("Gradient Color 2", "#0000FF")
            gradient_direction = st.selectbox("Gradient Direction", 
                                           ["to right", "to left", "to bottom", "to top", 
                                            "to bottom right", "to top left", "circle"])
            bg_style = f"background: linear-gradient({gradient_direction}, {gradient_color1}, {gradient_color2})"
        else:
            bg_style = f"background-color:{st.sidebar.color_picker('Pick Background color', '#654FEF')}"

        # Shape customization
        st.sidebar.subheader("Shape Customization")
        height = st.sidebar.slider('Height (px)', 50, 500, 150)
        width = st.sidebar.slider("Width (px)", 50, 500, 150)
        
        # ADVANCED FEATURE 2: Border customization with multiple sides
        st.sidebar.subheader("Border Settings")
        border_top = st.sidebar.slider("Top Border (px)", 0, 20, 1)
        border_right = st.sidebar.slider("Right Border (px)", 0, 20, 1)
        border_bottom = st.sidebar.slider("Bottom Border (px)", 0, 20, 1)
        border_left = st.sidebar.slider("Left Border (px)", 0, 20, 1)
        
        border_style = st.sidebar.selectbox("Border Style", ["solid", "dotted", "dashed", "double", "groove", "ridge"])
        border_color = st.sidebar.color_picker("Border Color", "#654FEF")
        
        # Corner radius
        st.sidebar.subheader("Corner Radius")
        top_left = st.sidebar.slider('Top Left', 0, 100, 10)
        top_right = st.sidebar.slider("Top Right", 0, 100, 10)
        bottom_left = st.sidebar.slider("Bottom Left", 0, 100, 10)
        bottom_right = st.sidebar.slider("Bottom Right", 0, 100, 10)

        # ADVANCED FEATURE 3: Box Shadow with opacity slider
        st.sidebar.subheader("Shadow Effects")
        shadow = st.sidebar.checkbox("Add Shadow")
        if shadow:
            shadow_h = st.sidebar.slider("Horizontal Shadow", -50, 50, 10)
            shadow_v = st.sidebar.slider("Vertical Shadow", -50, 50, 10)
            shadow_blur = st.sidebar.slider("Blur Radius", 0, 50, 5)
            shadow_spread = st.sidebar.slider("Spread", 0, 50, 0)
            shadow_color = st.sidebar.color_picker("Shadow Color", "#000000")
            shadow_opacity = st.sidebar.slider("Shadow Opacity", 0.0, 1.0, 0.5)
            
            # Convert to RGBA format for opacity
            shadow_rgba = f"rgba({int(shadow_color[1:3], 16)}, {int(shadow_color[3:5], 16)}, {int(shadow_color[5:7], 16)}, {shadow_opacity})"
            shadow_style = f"box-shadow: {shadow_h}px {shadow_v}px {shadow_blur}px {shadow_spread}px {shadow_rgba};"
        else:
            shadow_style = ""

        # Generate the shape
        html_design = f"""
        <div style="
            height:{height}px;
            width:{width}px;
            {bg_style};
            border-radius:{top_left}px {top_right}px {bottom_right}px {bottom_left}px;
            border:{border_top}px {border_style} {border_color};
            border-right:{border_right}px {border_style} {border_color};
            border-bottom:{border_bottom}px {border_style} {border_color};
            border-left:{border_left}px {border_style} {border_color};
            margin: 30px auto;
            {shadow_style}
        ">
        </div>
        """
        
        st.markdown(html_design, unsafe_allow_html=True)

        if st.checkbox("View CSS Code"):
            st.subheader("Generated CSS Code")
            st.code(html_design)

        # Random generator button
        if st.button("Generate Random Design"):
            st.rerun()

    elif choice == "About":
        st.subheader("About This App")
        st.info("""
        This is an advanced CSS shape generator created by Amna.
        You can create custom shapes with various styling options.
        """)
        st.text("Key Features:")
        st.markdown("""
        - Gradient backgrounds
        - Individual border controls
        - Shadow effects with opacity control
        - Precise corner radius adjustments
        """)
        st.success("Built with Streamlit")

if __name__ == '__main__':
    main()