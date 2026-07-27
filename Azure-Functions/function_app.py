import logging

import azure.functions as func
from openai import (
    APIConnectionError,
    APIStatusError,
    AuthenticationError,
    OpenAI,
    OpenAIError,
    RateLimitError,
)

MODEL = "gpt-4.1-mini"
PROMPT = "Just wish me a good day."

app = func.FunctionApp(
    http_auth_level=func.AuthLevel.ANONYMOUS
)

client = OpenAI()


@app.route(
    route="greeting",
    methods=["GET"],
)
def generate_greeting(req: func.HttpRequest) -> func.HttpResponse:
    """Generate and return a short AI-created greeting."""
    logging.info("Greeting endpoint received a request.")

    try:
        response = client.responses.create(
            model=MODEL,
            input=PROMPT,
        )

        return func.HttpResponse(
            body=response.output_text,
            status_code=200,
            mimetype="text/plain",
            charset="utf-8",
        )

    except AuthenticationError:
        logging.exception("OpenAI authentication failed.")
        return func.HttpResponse(
            "The AI service is not configured correctly.",
            status_code=500,
        )

    except RateLimitError:
        logging.exception("OpenAI rate limit or quota error.")
        return func.HttpResponse(
            "The AI service is temporarily unavailable.",
            status_code=503,
        )

    except APIConnectionError:
        logging.exception("Could not connect to OpenAI.")
        return func.HttpResponse(
            "The AI service could not be reached.",
            status_code=503,
        )

    except APIStatusError as error:
        logging.exception(
            "OpenAI returned HTTP status %s.",
            error.status_code,
        )
        return func.HttpResponse(
            "The AI service returned an unexpected response.",
            status_code=502,
        )

    except OpenAIError:
        logging.exception("OpenAI SDK error.")
        return func.HttpResponse(
            "The AI service encountered an error.",
            status_code=500,
        )

    except Exception:
        logging.exception("Unexpected Azure Function error.")
        return func.HttpResponse(
            "Unexpected server error.",
            status_code=500,
        )