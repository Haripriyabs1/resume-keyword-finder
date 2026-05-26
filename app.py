import streamlit as st
import PyPDF2
import string

st.title("Resume Keyword Finder")

keyword = st.text_area("Enter The Required Skills (comma-separated)")
resume = st.file_uploader("Upload The Resume", type=["pdf"])

text = ""

if resume is not None:

    if keyword.strip() == "":
        st.warning("Please enter required skills")

    else:

        keywordsplit = keyword.split(",")

        keywordlower = [
            key.strip().lower().translate(
                str.maketrans('', '', string.punctuation)
            )
            for key in keywordsplit
        ]

        try:
            reader = PyPDF2.PdfReader(resume)

            for page in reader.pages:
                text += page.extract_text()

        except:
            st.error("Error reading PDF file")

        text = text.translate(
            str.maketrans('', '', string.punctuation)
        )

        text = text.lower()

        score = 0

        st.subheader("Skill Match Results")

        for keys in keywordlower:

            if keys in text:
                st.success(f"{keys} Matched Successfully")
                score += 1

            else:
                st.error(f"{keys} Not Matched")

        percentage = (score / len(keywordlower)) * 100

        st.subheader("Final Resume Score")

        st.metric(
            "ATS Match Percentage",
            f"{percentage:.2f}%"
        )

        st.progress(int(percentage))