with open("index.html", "r", encoding="utf-8") as f:
    content = f.read()

old_img = '                       <div class="one-third js-fullheight order-md-last img" style="background-image:url(images/bg_1.png);">\n                        <div class="overlay"></div>\n                       </div>'

new_img = """<div class="one-third js-fullheight order-md-last d-flex flex-column align-items-center justify-content-center" style="background:linear-gradient(135deg,#1a1a2e,#16213e);padding:30px;gap:20px;">
  <div style="background:#0f0f23;border:2px solid #6366f1;border-radius:16px;padding:24px;width:90%;text-align:center;box-shadow:0 4px 24px rgba(99,102,241,0.3);">
    <div style="font-size:32px;margin-bottom:8px;">🧠</div>
    <h3 style="color:#6366f1;font-size:20px;font-weight:700;margin-bottom:6px;">QueryMind</h3>
    <p style="color:#ccc;font-size:13px;margin-bottom:12px;">AI-Powered SQL Learning & DB Assistant</p>
    <div style="display:flex;flex-wrap:wrap;gap:6px;justify-content:center;margin-bottom:14px;">
      <span style="background:#1e1e3f;color:#818cf8;padding:3px 10px;border-radius:20px;font-size:11px;">Claude AI</span>
      <span style="background:#1e1e3f;color:#818cf8;padding:3px 10px;border-radius:20px;font-size:11px;">PostgreSQL</span>
      <span style="background:#1e1e3f;color:#818cf8;padding:3px 10px;border-radius:20px;font-size:11px;">Node.js</span>
      <span style="background:#1e1e3f;color:#818cf8;padding:3px 10px;border-radius:20px;font-size:11px;">Razorpay</span>
    </div>
    <a href="https://querymind.mukeshaitools.com" target="_blank" style="background:#6366f1;color:#fff;padding:8px 20px;border-radius:8px;text-decoration:none;font-size:13px;font-weight:600;">Live Demo →</a>
  </div>
  <div style="background:#0f0f23;border:2px solid #f78166;border-radius:16px;padding:24px;width:90%;text-align:center;box-shadow:0 4px 24px rgba(247,129,102,0.3);">
    <div style="font-size:32px;margin-bottom:8px;">🎓</div>
    <h3 style="color:#f78166;font-size:20px;font-weight:700;margin-bottom:6px;">Student Corner</h3>
    <p style="color:#ccc;font-size:13px;margin-bottom:12px;">AI Learning Platform for Students</p>
    <div style="display:flex;flex-wrap:wrap;gap:6px;justify-content:center;margin-bottom:14px;">
      <span style="background:#2a1a1a;color:#f78166;padding:3px 10px;border-radius:20px;font-size:11px;">Claude AI</span>
      <span style="background:#2a1a1a;color:#f78166;padding:3px 10px;border-radius:20px;font-size:11px;">MCQ Practice</span>
      <span style="background:#2a1a1a;color:#f78166;padding:3px 10px;border-radius:20px;font-size:11px;">World Map</span>
      <span style="background:#2a1a1a;color:#f78166;padding:3px 10px;border-radius:20px;font-size:11px;">Razorpay</span>
    </div>
    <a href="https://student.mukeshaitools.com" target="_blank" style="background:#f78166;color:#fff;padding:8px 20px;border-radius:8px;text-decoration:none;font-size:13px;font-weight:600;">Live Demo →</a>
  </div>
</div>"""

content = content.replace(old_img, new_img)

with open("index.html", "w", encoding="utf-8") as f:
    f.write(content)

print("Replaced!" if "bg_1.png" not in open("index.html").read() else "NOT replaced")
