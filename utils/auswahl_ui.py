import streamlit as st


def show_selection_summary(selected_count, selected_per_row, SHORTS, dev_markings, dev_points, Bonus, job_markings):
    """
    Display the selection summary and additional information about the effects of selection.
    """
    if selected_count > 0:
        st.header("Auswahl:")
        for column_name, row_label in selected_per_row.items():
            try:
                row_label_int = int(row_label)  # Attempt to convert row_label to an integer
                if column_name in job_markings and row_label_int < 90:
                    st.info(
                        f"**{SHORTS[column_name].value}:** \t{row_label:<25} wird auf 90 angehoben (Haupteigenschaft)",
                        icon="🚨",
                    )
                    if column_name in dev_markings:
                        text_b = f"sorgt für **{dev_points.get_dev_points(90)}** Entwicklungspunkte"
                        text_c = f"erzeugt eine Bonus von **{Bonus.standard_bonus(90)}** aus dem Wert"
                        text_d = f"anstatt der {dev_points.get_dev_points(row_label)} für {row_label}"
                        text_e = f"anstatt der {Bonus.standard_bonus(row_label)} für {row_label}"
                        st.write(
                            f"""
                            - - {text_b}
                                - {text_d}
                            - - {text_c}
                                - {text_e}
                            """
                        )
                    else:
                        text_c = f"erzeugt eine Bonus von **{Bonus.standard_bonus(90)}** aus dem Wert"
                        text_e = f"anstatt der {Bonus.standard_bonus(row_label)} für {row_label}"
                        st.write(
                            f"""
                            - - {text_c}
                                - {text_e}
                            """
                        )
                else:
                    text_a = f"**{SHORTS[column_name].value}:** \t{row_label:<25}"
                    if SHORTS[column_name].name in dev_markings:
                        text_b = f"sorgt für **{dev_points.get_dev_points(row_label)}** Entwicklungspunkte"
                        text_c = f"erzeugt eine Bonus von **{Bonus.standard_bonus(row_label)}** aus dem Wert"
                        st.write(
                            f"""
                            - {text_a}
                                - {text_b}
                                - {text_c}
                            """
                        )
                    else:
                        text_c = f"erzeugt eine Bonus von **{Bonus.standard_bonus(row_label)}** aus dem Wert"
                        st.write(
                            f"""
                            - {text_a}
                                - {text_c}
                            """
                        )

            except ValueError:
                st.markdown(f"**kein Wert für:** {SHORTS[column_name].name} ({SHORTS[column_name].value})")