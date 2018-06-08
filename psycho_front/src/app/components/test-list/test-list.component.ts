import {Component, DoCheck } from '@angular/core';

@Component({
  selector: 'app-test-list',
  templateUrl: './test-list.component.html',
  styleUrls: ['./test-list.component.scss']
})
export class TestListComponent implements DoCheck {
  lang: number;
  selectedTag = 1;
  testsPhrase = ['Выберите тест или категорию, чтобы начать поиск психологического профиля',
    'Сиздин психологиялык кароо таап баштоо үчүн сыноого же категорияны тандап'];
  tags = [
    {id: 1, title: ['Все', 'Бардык']},
    {id: 2, title: ['Личность', 'Личность']},
    {id: 3, title: ['Бизнес', 'Ишкердик']}
  ];
  tests = [
    {
      id: 1,
      title: ['Моя личность 100 предметов', 'Менин Personality 100-пункт'],
      img: 'https://discovermyprofile.com/file/_all/leaves280.jpg',
      desc: ['Измеряет пять основных размеров личности и дает подробную обратную связь по BIG5 и Юнгианскому типу.',
      'Табиятын беш негизги багыттарын жана иш-чараларды Big5 жана Юнгга түрү боюнча толук баа берет'],
      time: 5,
      tags: [1, 2]
    }
  ];
  constructor() { }

  ngDoCheck() {
    this.lang = Number(localStorage.lang);
  }

  selectTag(id: number): void {
    this.selectedTag = id;
  }
}
