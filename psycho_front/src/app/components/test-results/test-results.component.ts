import { Component, DoCheck, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import {LanguageService} from "../../services/language.service";

@Component({
  selector: 'app-test-results',
  templateUrl: './test-results.component.html',
  styleUrls: ['./test-results.component.css'],
  providers: [LanguageService]
})
export class TestResultsComponent implements DoCheck, OnInit {
  lang: number;
  extraversion = 0;
  neuroticism = 0;
  openness = 0;
  consciousness = 0;
  friendly = 0;
  info = [];
  constructor(
    private router: Router,
    private langService: LanguageService
  ) { }

  ngOnInit() {
    // JSON.parse(localStorage.getItem('results'))
    setTimeout(() => {
      this.info = this.langService.getResults();
      const psychoParams = JSON.parse(localStorage.getItem('results'));

      this.extraversion = psychoParams.extraversion;
      this.neuroticism = psychoParams.neuroticism;
      this.openness = psychoParams.openness;
      this.consciousness = psychoParams.consciousness;
      this.friendly = psychoParams.friendly;
    }, 1000);

    setTimeout(() => {
      localStorage.removeItem('text-results');
      localStorage.removeItem('results');
    }, 3000)
  }

  ngDoCheck() {
    this.lang = Number(localStorage.lang);
  }

  changeTitle (title: string) :string {
    switch (title) {
      case ('extraversion'):
        return 'Экстраверсия';

      case ('neuroticism'):
        return 'Нейротизм';

      case ('openness '):
        return 'Открытость';

      case ('consciousness'):
        return 'Сознательность';

      case ('friendly'):
        return 'Доброжелательность';

      default:
        return title
    }
  }
}
