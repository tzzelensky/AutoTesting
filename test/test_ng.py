import pytest

@pytest.mark.flaky(reruns=2, reruns_delay=2)
def test_find_promo_event(open_system, create_promoevent):
    open_system.goto("https://release.goulash.tech/promoevent/promoevent/index")
    open_system.locator('#Promoevent__search_by_promocode').fill('AutoTest2121')
    open_system.get_by_role("button", name="Поиск").click()