import { Component, DoCheck } from '@angular/core';
import { LanguageService } from '../../../services/language.service';
declare function require(path: string);

@Component({
  selector: 'app-header',
  templateUrl: './header.component.html',
  styleUrls: ['./header.component.scss'],
  providers: [LanguageService]
})
export class HeaderComponent implements DoCheck {
  lang = 0;
  imagePath = require('../../../../img/AUCA-Logo-2-tier-Left-COL22.png');

  constructor(
    private langService: LanguageService
  ) {}

  changeLang(lang: number) {
    this.langService.changeLanguage(lang);
  }

  ngDoCheck() {
    // this.lang = Number(localStorage.lang);
  }
}
