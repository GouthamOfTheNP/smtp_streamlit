import streamlit as st
from send_email import send_email
from datetime import datetime
import time as t

print(t.strftime("%H:%M:%S"))

title = st.title("Anonymous Email Sender")

with st.form(key="my_form"):
	recipient = st.text_input("Recipients", help="Use commas to separate email addresses")
	recipients = [email.strip() for email in recipient.split(",") if email]
	subject = st.text_input("Subject")
	content = st.text_area("Content")
	schedule = st.checkbox("Scheduled email send")
	date = st.date_input("Date to send")
	time = st.time_input("Time to send (UTC)")
	if st.form_submit_button("Send"):
		recipients_sent = []
		if date and time:
			schedule_time = datetime.combine(date, time)
			current_datetime = datetime.now()
			if current_datetime >= schedule_time:
				for recipient in recipients:
					send_email(subject, content, recipient)
					recipients_sent.append(recipient)
				if len(recipients_sent) == len(recipients):
					st.success("All emails have been sent successfully!")
					if st.success:
						t.sleep(5)
						st.rerun()
		else:
			for recipient in recipients:
				send_email(subject, content, recipient)
				recipients_sent.append(recipient)
			if len(recipients_sent) == len(recipients):
				st.success("All emails have been sent successfully!")
				if st.success:
					t.sleep(5)
					st.rerun()
