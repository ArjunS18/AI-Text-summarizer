from flask import Flask, request, jsonify
from pydantic import ValidationError
from schemas.request_models import SummarizeRequest
from services.summarizer_service import summarize_text
import time

app = Flask(__name__)


@app.route("/health", methods=["GET"])
def health_check():
    return jsonify({"status": "ok"}), 200


@app.route("/summarize", methods=["POST"])
def summarize():
    start_time = time.time()

    try:
        # Parse incoming JSON
        request_data = request.get_json()

        if not request_data:
            return jsonify({"error": "Invalid or missing JSON body"}), 400

        # Validate using Pydantic
        validated_request = SummarizeRequest(**request_data)

        # Call service layer
        summary_result = summarize_text(validated_request)

        processing_time = round((time.time() - start_time) * 1000, 2)

        response = {
            "original_length": len(validated_request.text),
            "summary_length": len(summary_result),
            "summary": summary_result,
            "processing_time_ms": processing_time
        }

        return jsonify(response), 200

    except ValidationError as ve:
        return jsonify({
            "error": "Validation failed",
            "details": ve.errors()
        }), 422

    except Exception as e:
        return jsonify({
            "error": "Internal server error",
            "message": str(e)
        }), 500


if __name__ == "__main__":
    app.run(debug=True, port=5000)
