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
  // thanks = ['Спасибо!', 'Рахмат!'];
  // questionLabel = ['Отражающий вопрос:', 'Ойлуу суроо:'];
  // buttons = [
  //   {
  //     text: ['Пройти другой тест', 'Дагы бир Тест алып'],
  //   }
  //   // text: ['Поделиться через фейсбук', 'Фейсбукта бөлүшүү'],
  //   // text: ['Поделиться на Twitter', 'Twitter бөлүшүү'],
  // ];
  info = [];
  constructor(
    private router: Router,
    private langService: LanguageService
  ) { }

  ngOnInit() {
    this.info = [];
    setTimeout(() => {
      this.info = this.langService.getResults();
    }, 1000);

    setTimeout(() => {
      localStorage.removeItem('text-results');
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
