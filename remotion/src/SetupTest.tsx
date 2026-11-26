import { AbsoluteFill, interpolate, useCurrentFrame } from "remotion";

// 3-second vertical test used by /setup-tools to check that Remotion can render.
export const SetupTest: React.FC = () => {
  const frame = useCurrentFrame();
  const opacity = interpolate(frame, [0, 20], [0, 1], { extrapolateRight: "clamp" });
  return (
    <AbsoluteFill
      style={{
        backgroundColor: "#111",
        justifyContent: "center",
        alignItems: "center",
        color: "white",
        fontFamily: "sans-serif",
        fontSize: 120,
        fontWeight: 700,
        opacity,
      }}
    >
      Remotion works
    </AbsoluteFill>
  );
};
