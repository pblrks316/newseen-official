from flask import Flask, render_template, send_from_directory
import os

app = Flask(__name__, 
            static_folder='dist/assets',    # Folder untuk JS/CSS
            template_folder='dist')         # Folder untuk index.html

# 1. Route khusus untuk API (jika ada)

# 2. SATU-SATUNYA Catch-all Route untuk Frontend
@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def serve_vue(path):
    # Cek apakah path yang diminta adalah file fisik di folder 'dist'
    # Contoh: favicon.ico, logo.png, atau manifest.json
    full_path = os.path.join(app.template_folder, path)
    
    if path != "" and os.path.exists(full_path):
        return send_from_directory(app.template_folder, path)
    else:
        # Jika bukan file fisik (berarti route Vue seperti /login),
        # selalu kirim index.html
        return render_template("index.html")

if __name__ == '__main__':
    app.run(debug=True)