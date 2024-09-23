import streamlit as st
from send_email import send_email
import time

title = st.title("Anonymous Email Sender")


with st.form(key="my_form"):
	recipient = st.text_input("Recipients", help="Use commas to separate email addresses")
	recipients = [email.strip() for email in recipient.split(",") if email]
	subject = st.text_input("Subject")
	content = st.text_area("Content")
	if st.form_submit_button("Send"):
		recipients_sent = []
		for recipient in recipients:
			send_email(subject, content, recipient)
			recipients_sent.append(recipient)
		if len(recipients_sent) == len(recipients):
			st.success("All emails have been sent successfully!")
			if st.success:
				time.sleep(5)
				st.rerun()
