import sys
import pickle

def main():
    # Load the qa object from the file
    with open('qa_pipeline.pkl', 'rb') as f:
        qa = pickle.load(f)

    query = sys.argv[1] if len(sys.argv) > 1 else "Default Query"
    res = qa(query)
    answer = res["result"]

    print("\n> Question:")
    print(query)
    print("\n> Answer:")
    print(answer)

if __name__ == "__main__":
    main()
