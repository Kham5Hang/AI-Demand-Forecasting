if uploaded_file is not None:

    parser = FinproParser(uploaded_file)

    df = parser.read_excel()

    rows, cols = parser.get_sheet_size()

    st.success("File uploaded successfully!")

    col1, col2 = st.columns(2)

    col1.metric("Rows", rows)

    col2.metric("Columns", cols)

    st.subheader("Raw Data Preview")

    st.dataframe(parser.preview(), use_container_width=True)

else:

    st.info("Upload a FINPRO Sales Bill Register.")