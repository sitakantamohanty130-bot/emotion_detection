def emotion_detector(text_to_analyze):
    emotions = {
        "anger": 0.1,
        "disgust": 0.05,
        "fear": 0.2,
        "joy": 0.5,
        "sadness": 0.15
    }

    return (
        f"For the given text, the system response is:\n"
        f"anger: {emotions['anger']}, "
        f"disgust: {emotions['disgust']}, "
        f"fear: {emotions['fear']}, "
        f"joy: {emotions['joy']}, "
        f"sadness: {emotions['sadness']}"
    )


# test
if __name__ == "__main__":
    text = input("Enter text: ")
    print(emotion_detector(text))