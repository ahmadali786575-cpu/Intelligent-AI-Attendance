import streamlit as st


def subject_card(
    name,
    code,
    section,
    stats=None,
    footer_callback=None
):

    # ==========================================
    # SUBJECT CARD
    # ==========================================

    html = f"""
    <style>

        .subject-card {{
            width: 100%;
            height: 230px;

            box-sizing: border-box;

            background: white;

            border: 1px solid black;
            
            border-radius: 20px;

            padding: 25px;

            margin-bottom: 20px;

            overflow: hidden;
        }}

        .subject-card-content {{
            width: 100%;
            height: 100%;

            box-sizing: border-box;

            overflow-y: auto;
            overflow-x: hidden;

            padding-right: 8px;
        }}

        .subject-card-content h3 {{
            margin: 0 0 20px 0;

            color: #1e293b;

            font-size: 1.5rem;
            line-height: 1.35;

            overflow-wrap: anywhere;
            word-break: break-word;
        }}

        .subject-card-content p {{
            color: #64748b;

            margin: 10px 0 20px 0;
        }}

        .subject-code {{
            background: #E0E3FF;

            color: #5865F2;

            padding: 2px 8px;

            border-radius: 5px;
        }}

        .subject-stats {{
            display: flex;

            gap: 8px;

            flex-wrap: wrap;
        }}

        .subject-stat {{
            background: #EB459E10;

            padding: 5px 12px;

            border-radius: 12px;

            font-size: 0.9rem;

            white-space: nowrap;
        }}

    </style>


    <div class="subject-card">

        <div class="subject-card-content">

            <h3>
                {name}
            </h3>

            <p>
                Code :
                <span class="subject-code">
                    {code}
                </span>
                | Section : {section}
            </p>
    """

    # ==========================================
    # STATS
    # ==========================================

    if stats:

        html += """
            <div class="subject-stats">
        """

        for icon, label, value in stats:

            html += f"""
                <div class="subject-stat">
                    {icon}
                    <b>{value}</b>
                    {label}
                </div>
            """

        html += """
            </div>
        """

    # ==========================================
    # CLOSE HTML
    # ==========================================

    html += """
        </div>

    </div>
    """

    # ==========================================
    # IMPORTANT:
    # Use st.html(), NOT st.markdown()
    # ==========================================

    st.html(html)

    # ==========================================
    # FOOTER BUTTON
    # ==========================================

    if footer_callback:
        footer_callback()