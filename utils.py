def create_prompt(name, location, interests, style, version, service_description):
    return f"""
You are a professional email copywriter.

Write a concise, compelling **promotional email** to a person named **{name}**, living in **{location}**, who is interested in **{interests}**.

The tone/style should be **{style}**.

The email must promote this business:

**{service_description}**

📌 Format the output as:

**Subject: [A catchy subject line]**

**Body:**

[A compelling marketing email. Keep it concise. Use strong hooks, bold markdown for emphasis, and align the message with the person's interests.]

⚠️ Important:
- Focus strictly on the service: {service_description}.
- Do not mention that you're generating an A/B version.
- No extra explanations, bullets, or placeholders.
- Keep the tone {style}, aligned to the recipient’s interests.
"""
