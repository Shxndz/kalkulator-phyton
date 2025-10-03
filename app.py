from flask import Flask, request, render_template_string

app = Flask(__name__)

html = """
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Kalkulator Flask</title>
  <script src="https://cdn.tailwindcss.com"></script>
  <script>
    function appendValue(val) {
      document.getElementById("display").value += val;
    }
    function clearDisplay() {
      document.getElementById("display").value = "";
    }
    function calculate() {
      try {
        let result = eval(document.getElementById("display").value);
        document.getElementById("display").value = result;
      } catch {
        document.getElementById("display").value = "Error";
      }
    }
  </script>
</head>
<body class="bg-gradient-to-r from-gray-900 via-gray-800 to-gray-900 flex items-center justify-center min-h-screen text-white">
  <div class="bg-gray-800 p-6 rounded-2xl shadow-2xl w-80">
    <h1 class="text-2xl font-bold mb-4 text-center text-blue-400">🧮 Kalkulator</h1>
    
    <!-- Display -->
    <input id="display" readonly
           class="w-full text-right px-4 py-3 mb-4 rounded-lg text-black text-2xl font-mono shadow-inner bg-gray-200" />

    <!-- Buttons -->
    <div class="grid grid-cols-4 gap-3">
      <button onclick="clearDisplay()" class="col-span-2 bg-red-500 hover:bg-red-600 py-3 rounded-xl font-bold">C</button>
      <button onclick="appendValue('%')" class="bg-gray-600 hover:bg-gray-700 py-3 rounded-xl font-bold">%</button>
      <button onclick="appendValue('/')" class="bg-blue-500 hover:bg-blue-600 py-3 rounded-xl font-bold">÷</button>

      <button onclick="appendValue('7')" class="bg-gray-700 hover:bg-gray-600 py-3 rounded-xl font-bold">7</button>
      <button onclick="appendValue('8')" class="bg-gray-700 hover:bg-gray-600 py-3 rounded-xl font-bold">8</button>
      <button onclick="appendValue('9')" class="bg-gray-700 hover:bg-gray-600 py-3 rounded-xl font-bold">9</button>
      <button onclick="appendValue('*')" class="bg-blue-500 hover:bg-blue-600 py-3 rounded-xl font-bold">×</button>

      <button onclick="appendValue('4')" class="bg-gray-700 hover:bg-gray-600 py-3 rounded-xl font-bold">4</button>
      <button onclick="appendValue('5')" class="bg-gray-700 hover:bg-gray-600 py-3 rounded-xl font-bold">5</button>
      <button onclick="appendValue('6')" class="bg-gray-700 hover:bg-gray-600 py-3 rounded-xl font-bold">6</button>
      <button onclick="appendValue('-')" class="bg-blue-500 hover:bg-blue-600 py-3 rounded-xl font-bold">−</button>

      <button onclick="appendValue('1')" class="bg-gray-700 hover:bg-gray-600 py-3 rounded-xl font-bold">1</button>
      <button onclick="appendValue('2')" class="bg-gray-700 hover:bg-gray-600 py-3 rounded-xl font-bold">2</button>
      <button onclick="appendValue('3')" class="bg-gray-700 hover:bg-gray-600 py-3 rounded-xl font-bold">3</button>
      <button onclick="appendValue('+')" class="bg-blue-500 hover:bg-blue-600 py-3 rounded-xl font-bold">+</button>

      <button onclick="appendValue('0')" class="col-span-2 bg-gray-700 hover:bg-gray-600 py-3 rounded-xl font-bold">0</button>
      <button onclick="appendValue('.')" class="bg-gray-700 hover:bg-gray-600 py-3 rounded-xl font-bold">.</button>
      <button onclick="calculate()" class="bg-green-500 hover:bg-green-600 py-3 rounded-xl font-bold">=</button>
    </div>
  </div>
</body>
</html>
"""

@app.route("/")
def index():
    return render_template_string(html)

if __name__ == "__main__":
    app.run(debug=True)
