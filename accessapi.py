import sys

from openai import (
    APIConnectionError,
    APIStatusError,
    AuthenticationError,
    OpenAI,
    RateLimitError,
)

MODEL = "gpt-4.1-mini"


def generate_response(prompt: str) -> str:
    if not prompt.strip():
        raise ValueError("Prompt cannot be empty.")

    client = OpenAI()
    

    response = client.responses.create(
        model=MODEL,
        input=prompt,
    )

    return response.output_text


def main() -> None:
    try:
        output_text = generate_response("Just wish me a good day.")
        print(output_text)

    except AuthenticationError:
        print(
            "Authentication failed. Check the OPENAI_API_KEY environment variable.",
            file=sys.stderr,
        )
        sys.exit(1)

    except RateLimitError:
        print(
            "The request was rate-limited or the account has insufficient quota.",
            file=sys.stderr,
        )
        sys.exit(1)

    except APIConnectionError:
        print(
            "Could not connect to the OpenAI API. Check your internet connection.",
            file=sys.stderr,
        )
        sys.exit(1)

    except APIStatusError as error:
        print(
            f"OpenAI API error: HTTP {error.status_code}",
            file=sys.stderr,
        )
        sys.exit(1)

    except ValueError as error:
        print(str(error), file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()