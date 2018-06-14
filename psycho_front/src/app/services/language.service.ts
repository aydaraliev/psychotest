import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Observable } from 'rxjs/Observable';
import {QuestionsResponse} from '../classes/questionsResponse';
import { Response} from "../classes/response";
import {Voter} from "../classes/voter";

const httpOptions = {
  headers: new HttpHeaders({ 'Content-Type': 'application/json' })
};

@Injectable()
export class LanguageService {
  private apiUrl = 'http://188.166.88.156';  // URL to web
  object = null;
  textResults = null;

  constructor(
    private http: HttpClient,
  ) { }

  public lang = 0;

  getLanguage(): number {
    return this.lang;
  }

  changeLanguage(lang: number): void {
    this.lang = lang;
    localStorage.setItem('lang', `${lang}`);
  }

  getQuestions (id: number): Observable<QuestionsResponse> {
    const url = `${this.apiUrl}/tests/${id}`;
    return this.http.get<QuestionsResponse>(url);
  }

  saveResults (object: any) {
    return localStorage.setItem('results', JSON.stringify(object));
  };

  sendUser (object: any): Observable<Response> {
    const url = `${this.apiUrl}/tests/results`;
    const sendingObject = {
      user: object,
      results: JSON.parse(localStorage.getItem('results')),
      voter: JSON.parse(localStorage.getItem('voter'))
    };
    localStorage.removeItem('results');
    localStorage.removeItem('voter');
    return this.http.post<Response>(url, sendingObject, httpOptions);
  };

  findVoted (lastname: string, firstname: string): Observable<Voter> {
    const url = `${this.apiUrl}/tests/voter`;
    const sendingObject = { firstname, lastname };

    return this.http.post<Voter>(url, sendingObject, httpOptions)
  };

  getResults () {
    return JSON.parse(localStorage.getItem('text-results'));
  }
}
