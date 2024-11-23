
import pynecone as pc

from bs4 import BeautifulSoup


options = ['Rust', 'Python', 'Javascript', 'C++', 'Go' ]





class State(pc.State):
    lang: str = ''

def create_options(name):
    return pc.radio(name)


def index() -> pc.Component:
    return pc.center(

        pc.vstack(
            pc.heading(
                'Find Trending Repositories on Github', 
                color = 'white',
                size ='2xl', 
                font_weight = "bold",
            ),
            pc.spacer(),
            pc.spacer(),
            pc.spacer(),
            pc.spacer(),
            pc.radio_group(
                pc.hstack(
                    pc.foreach(
                        options,
                        create_options,
                        
                    ),
                    spacing = '2.5rem',
                ),
                display ='flex',
                color = 'white',
                align_items ='center',
                justify_content = 'center',
                on_change = State.set_lang,
            ),
        ),


        w='100%',
        height='100vh',
        bg='gray.900',
        display = 'flex',
        align_items='center',
        justify_content='center',
    )



app = pc.App(state=State)
app.add_page(index)
app.compile()
