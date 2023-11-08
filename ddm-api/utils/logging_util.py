import logging

def logger_config(log_level=logging.INFO, log_file="app.log"):
    """
    Konfigurer loggeren med ønsket loggnivå og filnavn.
    
    Args:
        log_level (int): Loggnivået for loggeren (f.eks. logging.INFO, logging.DEBUG).
        log_file (str): Filnavn for loggfiler.

    Returns:
        logger (logging.Logger): Logger-instans.
    """
    # Lag et formatteringsobjekt for loggeren
    log_formatter = logging.Formatter("%(asctime)s [%(levelname)s] [%(filename)s:%(lineno)d] - %(message)s")

    # Konfigurer loggeren
    logger = logging.getLogger("app_logger")
    logger.setLevel(log_level)

    # Opprett en filhandler for å lagre loggmeldinger i en fil
    file_handler = logging.FileHandler(log_file)
    file_handler.setLevel(log_level)
    file_handler.setFormatter(log_formatter)

    # Opprett en streamhandler for å sende loggmeldinger til konsollen
    stream_handler = logging.StreamHandler()
    stream_handler.setLevel(log_level)
    stream_handler.setFormatter(log_formatter)

    # Legg til filhandler og streamhandler i loggeren
    logger.addHandler(file_handler)
    logger.addHandler(stream_handler)

    return logger
