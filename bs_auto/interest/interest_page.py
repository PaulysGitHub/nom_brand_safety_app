from selenium.webdriver.common.by import By
from .base_elem import BaseElement
from .base_page import BasePage

class InterestPage(BasePage):

    url = 'https://brandsafety.nomdata.info'


    @property
    def edit_interest_link(self):
        locator = (By.CSS_SELECTOR, '#app-site > div > div > div.app-container.fixed-drawer > div > div > div > '
                                    'ul > li:nth-child(3) > a')
        return BaseElement(self.driver, by=locator[0], value=locator[1])

    @property
    def nom_logo(self):
        locator = (By.CSS_SELECTOR, "#app-site > div > div > div.app-container.fixed-drawer > div > div > div > "
                                    "div > a > img")
        return BaseElement(self.driver, by=locator[0], value=locator[1])

    @property
    def leaderboard_lnk_from_interest(self):
        locator = (By.CSS_SELECTOR, "#app-site > div > div > div.app-container.fixed-drawer > div > div > div > "
                                    "ul > li:nth-child(1) > a")
        return BaseElement(self.driver, by=locator[0], value=locator[1])

    @property
    def rate_videos_lnk_from_interest(self):
        locator = (By.CSS_SELECTOR, "#app-site > div > div > div.app-container.fixed-drawer > div > div > div > "
                                    "ul > li:nth-child(2) > a")
        return BaseElement(self.driver, by=locator[0], value=locator[1])

    @property
    def edit_interests_from_interest(self):
        locator = (By.CSS_SELECTOR, "#app-site > div > div > div.app-container.fixed-drawer > div > div > div > "
                                    "ul > li:nth-child(3) > a")
        return BaseElement(self.driver, by=locator[0], value=locator[1])

    @property
    def edit_profile_from_interest(self):
        locator = (By.CSS_SELECTOR, "#app-site > div > div > div.app-container.fixed-drawer > div > div > div > "
                                    "ul > li:nth-child(4) > a")
        return BaseElement(self.driver, by=locator[0], value=locator[1])

    @property
    def logout_from_interest(self):
        locator = (By.CSS_SELECTOR, "#app-site > div > div > div.app-container.fixed-drawer > div > div > div > "
                                    "ul > li:nth-child(5) > a")
        return BaseElement(self.driver, by=locator[0], value=locator[1])

    @property
    def interests_header_text(self):
        locator = (By.CSS_SELECTOR, '#app-site > div > div > div.app-main-content > div > div > div > div.gx-card '
                                    '> div.gx-card-header > div > div.col-md-9 > h3')
        return BaseElement(self.driver, by=locator[0], value=locator[1])

    @property
    def create_new_interest_btn(self):
        locator = (By.CSS_SELECTOR, "#app-site > div > div > div.app-main-content > div > div > div > div.gx-card > "
                                    "div.gx-card-header > div > div.col-md-3 > button")
        return BaseElement(self.driver, by=locator[0], value=locator[1])

    @property
    def create_interest_dropdown(self):
        locator = (By.CSS_SELECTOR, "#interests-data-table_length > label > select")
        return BaseElement(self.driver, by=locator[0], value=locator[1])

    @property
    def interest_show_entries_choose_10(self):
        locator = (By.CSS_SELECTOR, "#interests-data-table_length > label > select > option:nth-child(1)")
        return BaseElement(self.driver, by=locator[0], value=locator[1])

    @property
    def interest_show_entries_choose_25(self):
        locator = (By.CSS_SELECTOR, "#interests-data-table_length > label > select > option:nth-child(2)")
        return BaseElement(self.driver, by=locator[0], value=locator[1])

    @property
    def interest_show_entries_choose_50(self):
        locator = (By.CSS_SELECTOR, "#interests-data-table_length > label > select > option:nth-child(3)")
        return BaseElement(self.driver, by=locator[0], value=locator[1])

    @property
    def interest_show_entries_choose_100(self):
        locator = (By.CSS_SELECTOR, "#interests-data-table_length > label > select > option:nth-child(4)")
        return BaseElement(self.driver, by=locator[0], value=locator[1])

    @property
    def interest_show_entries_amount_results(self):
        locator= (By.CSS_SELECTOR, "#interests-data-table_info")
        return BaseElement(self.driver, by=locator[0], value=locator[1])

    # @property
    # def interest_search_text(self):
    #     locator = (By.CSS_SELECTOR, "")

    @property
    def interest_search_box(self):
        locator = (By.CSS_SELECTOR, "#interests-data-table_filter > label > input")
        return BaseElement(self.driver, by=locator[0], value=locator[1])

    @property
    def interest_catagory_science(self):
        locator = (By.CSS_SELECTOR, "#interests-data-table > tbody > tr:nth-child(1) > td.align-middle.sorting_1")
        return BaseElement(self.driver, by=locator[0], value=locator[1])

    @property
    def interest_catagory_poetry(self):
        locator = (By.CSS_SELECTOR, "#interests-data-table > tbody > tr > td.align-middle.sorting_1")
        return BaseElement(self.driver, by=locator[0], value=locator[1])

    @property
    def interest_datatable_header(self):
        locator = (By.CSS_SELECTOR, "#interests-data-table > thead > tr > th.sorting_asc")
        return BaseElement(self.driver, by=locator[0], value=locator[1])

    @property
    def interest_datatable_sort(self):
        locator = (By.CSS_SELECTOR, "#interests-data-table > thead > tr > th.sorting_asc")
        return BaseElement(self.driver, by=locator[0], value=locator[1])

    @property
    def interest_arts_entertainment(self):
        locator = (By.CSS_SELECTOR, "#interests-data-table > tbody > tr:nth-child(1) > td.align-middle.sorting_1")
        return BaseElement(self.driver, by=locator[0], value=locator[1])

    @property
    def arts_entertainment_text(self):
        locator = (By.CSS_SELECTOR, "#interests-data-table > tbody > tr:nth-child(1) > td.align-middle.sorting_1")
        return BaseElement(self.driver, by=locator[0], value=locator[1])

    @property
    def edit_interest_button_link(self):
        locator = (By.CSS_SELECTOR, "#interests-data-table > tbody > tr:nth-child(1) > td:nth-child(2) > a")

        return BaseElement(self.driver, by=locator[0], value=locator[1])

    # @property
    # def edit_interest_button_link_science(self):
    #     locator = (By.CSS_SELECTOR, "#interests-data-table > tbody > tr:nth-child(1) > td:nth-child(2) > a")

    @property
    def showing_entries(self):
        locator = (By.CSS_SELECTOR, "#interests-data-table_info")
        return BaseElement(self.driver, by=locator[0], value=locator[1])

    @property
    def previous_button(self):
        locator = (By.CSS_SELECTOR, "#interests-data-table_previous")
        return BaseElement(self.driver, by=locator[0], value=locator[1])

    @property
    def next_button(self):
        locator = (By.CSS_SELECTOR, "#interests-data-table_next > a")
        return BaseElement(self.driver, by=locator[0], value=locator[1])

    @property
    def second_page_button(self):
        locator = (By.CSS_SELECTOR, "#interests-data-table_paginate > ul > li:nth-child(3) > a")
        return BaseElement(self.driver, by=locator[0], value=locator[1])

    @property
    def first_page_button(self):
        locator = (By.CSS_SELECTOR, "#interests-data-table_paginate > ul > li:nth-child(2) > a")
        return BaseElement(self.driver, by=locator[0], value=locator[1])

# Interest Page Stats
    @property
    def suggest_tags_button_link(self):
        locator = (By.CSS_SELECTOR, "#app-site > div > div > div.app-main-content > div > div > div > div > div.col-3 > div > div > div:nth-child(2) > div.col-sm-10.text-center > a")
        return BaseElement(self.driver, by=locator[0], value=locator[1])

    @property
    def interest_title(self):
        locator = (By.CSS_SELECTOR, "#app-site > div > div > div.app-main-content > div > "
                                    "div > div > div > div.col-3 > div > div > div:nth-child(1) > div > h1")
        return BaseElement(self.driver, by=locator[0], value=locator[1])

    @property
    def datatable_tag_name_header(self):
        locator = (By.CSS_SELECTOR, "#suggested-tags-table > thead > tr > th:nth-child(1)")
        return BaseElement(self.driver, by=locator[0], value=locator[1])

    @property
    def datatable_system_tag_header(self):
        locator = (By.CSS_SELECTOR, "#suggested-tags-table > thead > tr > th:nth-child(2)")
        return BaseElement(self.driver, by=locator[0], value=locator[1])


# Suggest Tags Page

    @property
    def interest_title_header(self):
        locator = (By.CSS_SELECTOR, "#app-site > div > div > div.app-main-content > div > div > div > div:nth-child(1) "
                                    "> div.col-md-7 > div > div > div > div.col-sm-9 > h2")
        return BaseElement(self.driver, by=locator[0], value=locator[1])

    @property
    def interest_text_instructions(self):
        locator = (By.CSS_SELECTOR, "#app-site > div > div > div.app-main-content > div > div > div > div:nth-child(1) "
                                    "> div.col-md-7 > div > div > div > div.col-sm-9 > p")
        return BaseElement(self.driver, by=locator[0], value=locator[1])

    @property
    def go_back_button(self):
        locator = (By.CSS_SELECTOR, "#app-site > div > div > div.app-main-content > div > div > div > "
                                    "div:nth-child(1) > div.col-md-7 > div > div > div > div.col-sm-3 > a")
        return BaseElement(self.driver, by=locator[0], value=locator[1])

    @property
    def interest_current_tags(self):
        locator = (By.CSS_SELECTOR, "#app-site > div > div > div.app-main-content > div > div > div > div:nth-child(1) "
                                    "> div.col-md-7 > div > div > div > div.col-sm-9 > h3")
        return BaseElement(self.driver, by=locator[0], value=locator[1])

    @property
    def tags_research_title(self):
        locator = (By.CSS_SELECTOR, "#app-site > div > div > div.app-main-content > div > div > div > div:nth-child(1) "
                                    "> div.col-md-5 > div > div.gx-card-header > h3")
        return BaseElement(self.driver, by=locator[0], value=locator[1])

    @property
    def tags_research_text_instructions(self):
        locator = (By.CSS_SELECTOR, "#tagsSuggest > form > div.form-group.row > p")
        return BaseElement(self.driver, by=locator[0], value=locator[1])

    @property
    def tags_research_text_box(self):
        locator = (By.CSS_SELECTOR, "#tagsSuggest > form > div.form-group.row > span > span.selection > span > ul")
        return BaseElement(self.driver, by=locator[0], value=locator[1])

    @property
    def tags_research_clear_list_btn(self):
        locator = (By.CSS_SELECTOR, "#tagsSuggest > form > div:nth-child(2) > div > div.col-4 > button")
        return BaseElement(self.driver, by=locator[0], value=locator[1])

    @property
    def tags_suggest_tags_btn(self):
        locator = (By.CSS_SELECTOR, "#tagsSuggest > form > div:nth-child(2) > div > div.col-8 > button")
        return BaseElement(self.driver, by=locator[0], value=locator[1])

    @property
    def suggested_tags_header(self):
        locator = (By.CSS_SELECTOR, "#app-site > div > div > div.app-main-content > div > div > div > "
                                    "div:nth-child(2) > div > div > div.gx-card-header > h3")
        return BaseElement(self.driver, by=locator[0], value=locator[1])

    @property
    def suggested_dropdown(self):
        locator = (By.CSS_SELECTOR, "#suggested-tags-table_length > label > select")
        return BaseElement(self.driver, by=locator[0], value=locator[1])

    @property
    def suggested_tags_search_box(self):
        locator = (By.CSS_SELECTOR, "#suggested-tags-table_filter > label > input")
        return BaseElement(self.driver, by=locator[0], value=locator[1])

    @property
    def suggested_tags_tag_name_datatable_header(self):
        locator = (By.CSS_SELECTOR, "#suggested-tags-table > thead > tr > th:nth-child(1)")
        return BaseElement(self.driver, by=locator[0], value=locator[1])

    @property
    def suggested_tags_system_tag_datatable_header(self):
        locator = (By.CSS_SELECTOR, "#suggested-tags-table > thead > tr > th:nth-child(2)")
        return BaseElement(self.driver, by=locator[0], value=locator[1])

    @property
    def suggested_tags_score_datatable_header(self):
        locator = (By.CSS_SELECTOR, "#suggested-tags-table > thead > tr > th.text-center.sorting_desc")
        return BaseElement(self.driver, by=locator[0], value=locator[1])

    @property
    def suggested_tags_matched_datatable_header(self):
        locator = (By.CSS_SELECTOR, "#suggested-tags-table > thead > tr > th:nth-child(4)")
        return BaseElement(self.driver, by=locator[0], value=locator[1])

    @property
    def suggested_tags_top_matches_datatable_header(self):
        locator = (By.CSS_SELECTOR, "#suggested-tags-table > thead > tr > th:nth-child(5)")
        return BaseElement(self.driver, by=locator[0], value=locator[1])

    @property
    def suggested_tags_show_entries_results(self):
        locator = (By.CSS_SELECTOR, "#suggested-tags-table_info")
        return BaseElement(self.driver, by=locator[0], value=locator[1])

    @property
    def suggested_tags_previous_btn(self):
        locator = (By.CSS_SELECTOR, "#suggested-tags-table_previous")
        return BaseElement(self.driver, by=locator[0], value=locator[1])

    @property
    def suggested_tags_next_btn(self):
        locator = (By.CSS_SELECTOR, "#suggested-tags-table_next")
        return BaseElement(self.driver, by=locator[0], value=locator[1])

    # Add the datatable sorters ascending/descending here...

