import { Component, DoCheck } from '@angular/core';
import { LanguageService } from '../../../services/language.service';

@Component({
  selector: 'app-header',
  templateUrl: './header.component.html',
  styleUrls: ['./header.component.scss'],
  providers: [LanguageService]
})
export class HeaderComponent implements DoCheck {
  lang = 0;
  moreTests = ['Больше тестов', 'Көбүрөөк тесттер'];

  constructor(
    private langService: LanguageService
  ) {}

  changeLang(lang: number) {
    this.langService.changeLanguage(lang);
  }

  ngDoCheck() {
    this.lang = Number(localStorage.lang);
  }
}
