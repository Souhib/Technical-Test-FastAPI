from sqlmodel import Session, SQLModel, create_engine
import numpy as np
import pandas as pd
from api.models.frame import Frame
from api.settings import Settings


settings = Settings()

engine = create_engine(settings.database_url)

SQLModel.metadata.create_all(engine)


def resize_image(frame, original_width=200, target_width=150):
    """
    Resizes a given frame to a target width while maintaining the original aspect ratio.

    This function takes a frame, its original width, and a target width as input. It calculates
    the indices for the target width using numpy's linspace function and returns the resized
    frame as a list.

    Args:
        frame (numpy.ndarray): The frame to be resized.
        original_width (int, optional): The original width of the frame. Defaults to 200.
        target_width (int, optional): The target width for the resized frame. Defaults to 150.

    Returns:
        list: The resized frame as a list of integers.
    """
    indices = np.linspace(0, original_width - 1, num=target_width, dtype=int)
    return frame[indices].tolist()


def store_frames_sqlmodel(file_path):
    """
    Reads a CSV file, resizes the frames, and stores them in the database.

    This function reads a CSV file containing frame data, cleans the data by filling NaN values,
    resizes each frame to a target width, and stores the resized frames along with their depth
    information in the database using SQLModel.

    Args:
        file_path (str): The path to the CSV file containing frame data.
    """
    data = pd.read_csv(file_path)
    data_cleaned = data.fillna(0)

    with Session(engine) as session:
        for _, row in data_cleaned.iterrows():
            depth = row["depth"]
            frame = row.iloc[1:].values.astype(np.uint8)
            resized_frame = resize_image(frame)
            frame_record = Frame(depth=depth, frame=resized_frame)
            session.add(frame_record)

        session.commit()


if __name__ == "__main__":
    store_frames_sqlmodel("img.csv")
