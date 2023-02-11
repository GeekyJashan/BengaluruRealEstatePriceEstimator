from flask import Flask, request, jsonify
import util
print(request.form.get('location'))