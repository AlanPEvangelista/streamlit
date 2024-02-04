import streamlit as st
import time
import datetime


def main():
    st.title("Cronômetro Digital")

    if "start_time" not in st.session_state:
        st.session_state.start_time = None
        st.session_state.elapsed_time = 0

    start_stop_button = st.button("Iniciar/Pausar")

    if start_stop_button:
        if st.session_state.start_time is None:
            st.session_state.start_time = time.time()
        else:
            st.session_state.elapsed_time += time.time() - st.session_state.start_time
            st.session_state.start_time = None

    reset_button = st.button("Reiniciar")

    if reset_button:
        st.session_state.start_time = time.time()
        st.session_state.elapsed_time = 0

    elapsed_time = get_elapsed_time()

    formatted_elapsed_time = format_time(elapsed_time)
    st.write(f"Tempo Decorrido: {formatted_elapsed_time}")

    st.text("")  # Adiciona um espaço vazio para forçar a atualização

    if st.session_state.start_time is not None:
        st.experimental_rerun()


def get_elapsed_time():
    if st.session_state.start_time is not None:
        return st.session_state.elapsed_time + time.time() - st.session_state.start_time
    else:
        return st.session_state.elapsed_time


def format_time(seconds):
    minutes, seconds = divmod(seconds, 60)
    return "{:02}:{:02}".format(int(minutes), int(seconds))


if __name__ == "__main__":
    main()
