import streamlit as st

if st.button("Refresh"):
  st.cache_resource.clear()
  st.rerun()

questions = [1,2,3]

num1 = [1,2,3]
num2 = [4,5,6]

for question in questions:
    
    with st.form("Question",question):
        st.write("Question number: ", question)
        
        n1 = num1[question]
        n2 = num2[question]

        sum = n1 + n2
        
        st.write(n1," + ", n2)
        ans=st.number_input(" Enter your answer",step=1)
        
        submitted = st.form_submit_button("Submit")
        if submitted:
            st.write("Question: ", n1, " + ", n2)
            st.write("Actual Answer: ", sum)
            st.write("Your Answer: ", ans)
            
            if ans==sum:
                st.write( " YAY YOU ARE CORRRRRRRREEEEEECCCCCCTTTTTTTTTTTTTTTTTT")
            else:
                st.write(" YOU GET A RED CAAAAAAAAARRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRD")

    st.write("Outside the form")
