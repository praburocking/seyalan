import { atom } from "recoil";

export const user = atom({
  key: "user",
  default: {},
});

export const org = atom({
    key: "org",
    default: {},
  });

  export const license = atom({
    key: "license",
    default: {},
  });

  export const auth = atom({
    key: "auth",
    default: '',
  });

  export const test=atom({
    key:"test",
    default:0
  })