import { AnimalShelterUiPage } from './app.po';

describe('animal-shelter-ui App', () => {
  let page: AnimalShelterUiPage;

  beforeEach(() => {
    page = new AnimalShelterUiPage();
  });

  it('should display message saying app works', () => {
    page.navigateTo();
    expect(page.getParagraphText()).toEqual('app works!');
  });
});
