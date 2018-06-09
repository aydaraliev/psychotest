import { Component, DoCheck } from '@angular/core';
import { Router } from '@angular/router';
// import { Info} from '../../classes/info';

@Component({
  selector: 'app-test-results',
  templateUrl: './test-results.component.html',
  styleUrls: ['./test-results.component.css']
})
export class TestResultsComponent implements DoCheck {
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
  info = JSON.parse(localStorage.getItem('textResults'));
  constructor(
    private router: Router
  ) { }

  ngDoCheck() {
    this.lang = Number(localStorage.lang);
  }
}
