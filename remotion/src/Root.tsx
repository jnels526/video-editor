import { Composition } from "remotion";
import { MyComposition } from "./Composition";
import { SetupTest } from "./SetupTest";

export const RemotionRoot: React.FC = () => {
  return (
    <>
      <MyComposition />
      <Composition
        id="SetupTest"
        component={SetupTest}
        durationInFrames={90}
        fps={30}
        width={1080}
        height={1920}
      />
    </>
  );
};
