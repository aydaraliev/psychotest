import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Observable } from 'rxjs/Observable';
import {QuestionsResponse} from '../classes/questionsResponse';

const httpOptions = {
  headers: new HttpHeaders({ 'Content-Type': 'application/json' })
};

@Injectable()
export class LanguageService {
  private apiUrl = 'http://127.0.0.1:5000';  // URL to web
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

  getResultsText (object: any): Observable<Object> {
    const url = `${this.apiUrl}/results`;
    console.log(object)

    return this.http.get<Object>(url, object);
  }

  sendUser (object: any): Observable<Object> {
    const url = `${this.apiUrl}/user`;
    const sendingObject = {
      user: object,
      results: JSON.parse(localStorage.getItem('results'))
    };
    console.log(sendingObject)
    localStorage.removeItem('results')
    return this.http.post<Object>(url, sendingObject, httpOptions);
  }

  saveResultsText (object: any) {
    this.textResults = object;
  }
}
