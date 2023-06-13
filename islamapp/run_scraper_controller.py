from scraper.scraper_controller import ScraperCotroller
import logging

status_logger = logging.getLogger("STATUS_LOGGER")
status_handler = logging.FileHandler("logs/status.log")
status_handler.setLevel(logging.INFO)
status_logger.addHandler(status_handler)

mission_logger = logging.getLogger("MISSION_LOGGER")
mission_handler = logging.FileHandler("logs/mission.log")
mission_handler.setLevel(logging.INFO)
mission_logger.addHandler(mission_handler)

logging.basicConfig(
    filename="logs/log.log",
    level=logging.DEBUG,
    format="%(asctime)s %(levelname)s: %(message)s",
)


if __name__ == "__main__":
    scraper_controller = ScraperCotroller(
        status_logger,
        mission_logger,
        run_period=1,
        run_local=True,
        local_driver_limit=4,
    )
    scraper_controller.run()
