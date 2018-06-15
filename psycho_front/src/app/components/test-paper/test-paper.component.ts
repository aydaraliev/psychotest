import {Component, DoCheck, OnInit} from '@angular/core';
import { Router } from '@angular/router';
import { Question } from '../../classes/question';
import { Answer } from '../../classes/answer';
import { LanguageService } from '../../services/language.service';

@Component({
  selector: 'app-test-paper',
  templateUrl: './test-paper.component.html',
  styleUrls: ['./test-paper.component.scss'],
  providers: [LanguageService]
})

export class TestPaperComponent implements OnInit, DoCheck {
  lang: number;
  questions = [];
  answers: any;
  title: any;
  count = 0;
  currentQuestion: number;
  currentPercent: number;
  extraversion = 0;
  neuroticism = 0;
  openness = 0;
  consciousness = 0;
  friendly = 0;

  constructor(
    private langService: LanguageService,
    private router: Router
  ) { }

  ngOnInit() {
    window.scrollTo(0, 0);
    this.currentQuestion = 0;
    this.lang = this.langService.getLanguage();
    this.answers = [
      {title: ['Нет, это не обо мне', ''], value: 0},
      {title: ['Иногда это обо мне, иногда — нет', ''], value: 1},
      {title: ['Да, это точно обо мне', ' '], value: 2}
    ];

    this.langService.getQuestions(1)
      .subscribe(
        response => {
          this.title = response.name;
          this.questions = response.questions;
        },
        error => console.log(error)
      );
    }

  ngDoCheck() {
    // this.lang = Number(localStorage.lang);
  }

  /**
   * Setting value for question
   * @param {number} value - value of answer
   */
  onAnswer(value: number): void {
    this.calculateProgress();
    if (this.currentQuestion !== this.questions.length - 1) {
      this.questions[this.currentQuestion].value = value;
      this.currentQuestion += 1;
      this.calculateResults();
    } else {
      this.questions[this.currentQuestion].value = value;
      this.calculateResults();
      const sendingObject = {
        extraversion: this.extraversion,
        neuroticism: this.neuroticism,
        openness: this.openness,
        consciousness: this.consciousness,
        friendly: this.friendly
      };

      this.langService.saveResults(sendingObject);

      this.router.navigate(['/voted']);
    }
  }

  onForward(): void {
    if (this.currentQuestion !== this.questions.length - 1) {
      this.currentQuestion = 1;
    }
  }

  onBack(): void {
    if (this.currentQuestion !== 0) {
      this.currentQuestion -= 1;
    }
  }

  calculateProgress(): void {
    this.count += 1;
    this.currentPercent = this.count * 100 / this.questions.length;
  }

  calculateResults(): void {
    const id = this.questions[this.currentQuestion - 1].question_number;
    const value = this.questions[this.currentQuestion - 1].value;

    if ((id + 4) % 5 === 0) {
      this.extraversion += ((value * 100) / 16);
    }

    if ((id + 3) % 5 === 0) {
      this.neuroticism += ((value * 100) / 16);
    }

    if ((id + 2) % 5 === 0) {
      this.openness += ((value * 100) / 16);
    }

    if ((id + 1) % 5 === 0) {
      this.consciousness += ((value * 100) / 16);
    }

    if (id % 5 === 0) {
      this.friendly += ((value * 100) / 16);
    }
  }

}
