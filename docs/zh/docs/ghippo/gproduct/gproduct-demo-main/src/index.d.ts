interface Window {
  __POWERED_BY_QIANKUN__?: boolean;
  __INJECTED_PUBLIC_PATH_BY_QIANKUN__: string;
  // eslint-disable-next-line camelcase
}

declare interface QiankunProps {
  container?: HTMLElement;
  routerBase?: string;
  sharedStore?: SharedStore;
  onGlobalStateChange?: (arg0: (state: unknown, prev: unknown) => void) => void;
  setGlobalState?: (arg0: { [string]: unknown }) => void;
  basePath?: string;
}
