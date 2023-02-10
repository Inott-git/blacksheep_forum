from blacksheep import use_templates
from jinja2 import PackageLoader
from roconfiguration import Configuration
from rodi import Container
from blacksheep.server import Application
from app import controllers  # NoQA


from app.templating import configure_templating


async def before_start(application: Application) -> None:
    application.services.add_instance(application)
    application.services.add_alias("app", Application)


def configure_application() -> Application:
    app = Application(
        show_error_details=True,
        debug=True,
    )

    app.on_start += before_start
    configure_templating(app)
    app.serve_files("app/static")
    return app
