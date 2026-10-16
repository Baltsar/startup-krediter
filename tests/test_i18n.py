"""Generated labels and questions: every language covers every field, and a label says only what the rule checks."""

from __future__ import annotations

import pytest

import i18n

FIELDS = set(i18n.LABELS["en"])


@pytest.mark.parametrize("lang", i18n.LANGS)
def test_every_language_covers_every_field_op_and_phrase(lang: str) -> None:
    assert set(i18n.LABELS[lang]) == FIELDS, lang
    for field in FIELDS:
        assert set(i18n.LABELS[lang][field]) == set(i18n.LABELS["en"][field]), (lang, field)
    assert set(i18n.QUESTIONS[lang]) == set(i18n.QUESTIONS["en"]), lang
    assert set(i18n.PHRASES[lang]) == set(i18n.PHRASES["en"]), lang
    for table in (i18n.COUNTRY_NAMES, i18n.LEGAL_FORM_NAMES, i18n.STAGE_NAMES, i18n.SECTOR_NAMES):
        assert set(table[lang]) == set(table["en"]), (lang, table)


def test_country_label_is_a_place_not_a_nationality_or_a_company() -> None:
    rule = {"field": "country", "op": "eq", "value": "SE"}
    assert i18n.rule_label(rule, "en") == "in Sweden"
    assert i18n.rule_label(rule, "sv") == "i Sverige"
    assert i18n.rule_label(rule, "fi") == "Ruotsissa"
    assert i18n.rule_label(rule, "no") == "i Sverige"
    assert i18n.rule_label(rule, "da") == "i Sverige"


def test_residence_label_is_about_the_founders() -> None:
    rule = {"field": "residence_country", "op": "in", "value": ["DK", "SE"]}
    assert i18n.rule_label(rule, "en") == "founders based in Denmark or Sweden"
    assert i18n.rule_label(rule, "sv") == "grundarna bor i Danmark eller Sverige"


def test_stage_label_names_the_stages_and_nothing_else() -> None:
    """The old data said 'early research spinout' for this rule. The generated label cannot."""
    rule = {"field": "stage", "op": "in", "value": ["idea", "pre_seed", "seed"]}
    assert i18n.rule_label(rule, "en") == "stage: idea, pre-seed or seed"
    assert i18n.rule_label(rule, "sv") == "fas: idé, pre-seed eller seed"
    assert i18n.rule_question(rule, "sv") == "Vilken fas: idé, pre-seed, seed, serie A, eller senare?"


def test_numbers_are_formatted_with_spaces_in_every_language() -> None:
    rule = {"field": "funding_raised_usd", "op": "gt", "value": 1000000}
    for lang in i18n.LANGS:
        assert "1 000 000 USD" in i18n.rule_label(rule, lang), lang
    assert i18n.rule_label({"field": "employees", "op": "lte", "value": 249}, "en") == "at most 249 employees"
    assert i18n.rule_label({"field": "balance_meur", "op": "lte", "value": 2.5}, "en") == "balance sheet at most 2.5 MEUR"


def test_boolean_rules_read_as_facts() -> None:
    assert i18n.rule_label({"field": "has_vat", "op": "eq", "value": True}, "en") == "VAT number"
    assert i18n.rule_label({"field": "profit_distributed", "op": "eq", "value": False}, "sv") == "ingen vinstutdelning förra året"
    assert i18n.rule_label({"field": "has_vat", "op": "neq", "value": True}, "en") == "no VAT number"


def test_contains_rules_name_the_vendor_or_sector() -> None:
    assert i18n.rule_label({"field": "stack", "op": "contains", "value": "anthropic"}, "en") == "uses Anthropic"
    assert i18n.rule_question({"field": "stack", "op": "contains", "value": "gcp"}, "sv") == "Använder ni Google Cloud?"
    assert i18n.rule_label({"field": "sector", "op": "contains", "value": "deeptech"}, "fi") == "toimiala: deep tech"


def test_group_label_joins_members_with_or() -> None:
    members = [{"field": "revenue_msek", "op": "lte", "value": 10}, {"field": "balance_msek", "op": "lte", "value": 10}]
    assert i18n.group_label(members, "en") == "revenue at most 10 MSEK, or balance sheet at most 10 MSEK"
    assert i18n.group_label(members, "no") == "omsetning høyst 10 MSEK, eller balansesum høyst 10 MSEK"


def test_unknown_language_falls_back_to_english() -> None:
    assert i18n.pick_lang("de") == "en"
    assert i18n.pick_lang("SV") == "sv"
    assert i18n.pick_lang(None) == "en"


def test_unknown_template_falls_back_to_plain_terms_instead_of_hiding_the_check() -> None:
    assert i18n.rule_label({"field": "stack", "op": "eq", "value": "aws"}, "en") == "stack eq aws"


@pytest.mark.parametrize("lang", i18n.LANGS)
def test_every_confirmation_has_every_language(lang: str) -> None:
    for key, entry in i18n.CONFIRMATIONS.items():
        assert lang in entry, (key, lang)
        label, question = entry[lang]
        assert label and question.endswith("?"), (key, lang)


def test_confirmation_rule_reads_as_the_stated_requirement() -> None:
    rule = {"field": "confirmed", "op": "contains", "value": "kth_affiliation"}
    assert i18n.rule_label(rule, "en") == "a current KTH student, researcher or employee on the team"
    assert i18n.rule_question(rule, "sv") == "Är någon av er student, forskare eller anställd på KTH just nu?"
    unknown = {"field": "confirmed", "op": "contains", "value": "mystery_key"}
    assert i18n.rule_label(unknown, "en") == "mystery_key"
