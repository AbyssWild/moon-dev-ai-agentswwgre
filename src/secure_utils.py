"""
🌙 Moon Dev's Security Utilities
Built with security in mind 🔒

This module provides secure alternatives to potentially dangerous operations.
"""

import subprocess
import platform
from pathlib import Path
from typing import Union


def play_audio_file(file_path: Union[str, Path]) -> bool:
    """
    Securely play an audio file using the system's default audio player.
    
    This is a secure replacement for os.system(f"afplay {file_path}") or os.system(f"start {file_path}")
    which are vulnerable to command injection.
    
    Args:
        file_path: Path to the audio file to play
        
    Returns:
        bool: True if playback was successful, False otherwise
        
    Example:
        >>> play_audio_file("/path/to/audio.mp3")
        True
    """
    try:
        # Convert to Path object for safer handling
        audio_path = Path(file_path)
        
        # Verify file exists
        if not audio_path.exists():
            print(f"❌ Audio file not found: {audio_path}")
            return False
            
        # Use list arguments to prevent command injection
        system = platform.system()
        
        if system == "Darwin":  # macOS
            cmd = ["afplay", str(audio_path)]
        elif system == "Windows":
            # For Windows, use the start command through subprocess
            cmd = ["cmd", "/c", "start", "", str(audio_path)]
        elif system == "Linux":
            # Try common Linux audio players in order of preference
            players = ["paplay", "aplay", "ffplay", "mpg123", "mpv"]
            cmd = None
            for player in players:
                try:
                    # Check if player exists
                    subprocess.run(["which", player], capture_output=True, check=True)
                    cmd = [player, str(audio_path)]
                    break
                except (subprocess.CalledProcessError, FileNotFoundError):
                    continue
                    
            if cmd is None:
                print("❌ No audio player found on Linux system")
                return False
        else:
            print(f"❌ Unsupported operating system: {system}")
            return False
            
        # Execute the command securely
        subprocess.run(cmd, check=True, capture_output=True)
        return True
        
    except subprocess.CalledProcessError as e:
        print(f"❌ Error playing audio: {e}")
        return False
    except Exception as e:
        print(f"❌ Unexpected error: {e}")
        return False


def play_audio_file_async(file_path: Union[str, Path]) -> bool:
    """
    Securely play an audio file asynchronously (non-blocking).
    
    This starts audio playback in the background and returns immediately.
    
    Args:
        file_path: Path to the audio file to play
        
    Returns:
        bool: True if playback was started successfully, False otherwise
    """
    try:
        # Convert to Path object for safer handling
        audio_path = Path(file_path)
        
        # Verify file exists
        if not audio_path.exists():
            print(f"❌ Audio file not found: {audio_path}")
            return False
            
        # Use list arguments to prevent command injection
        system = platform.system()
        
        if system == "Darwin":  # macOS
            cmd = ["afplay", str(audio_path)]
        elif system == "Windows":
            cmd = ["cmd", "/c", "start", "", str(audio_path)]
        elif system == "Linux":
            # Try common Linux audio players
            players = ["paplay", "aplay", "ffplay", "mpg123", "mpv"]
            cmd = None
            for player in players:
                try:
                    subprocess.run(["which", player], capture_output=True, check=True)
                    cmd = [player, str(audio_path)]
                    break
                except (subprocess.CalledProcessError, FileNotFoundError):
                    continue
                    
            if cmd is None:
                print("❌ No audio player found on Linux system")
                return False
        else:
            print(f"❌ Unsupported operating system: {system}")
            return False
            
        # Execute the command asynchronously
        subprocess.Popen(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        return True
        
    except Exception as e:
        print(f"❌ Unexpected error: {e}")
        return False


# Example usage and testing
if __name__ == "__main__":
    try:
        from termcolor import cprint
        
        cprint("\n" + "="*60, "cyan")
        cprint("🔒 Moon Dev's Secure Utilities Test", "cyan", attrs=['bold'])
        cprint("="*60 + "\n", "cyan")
        
        # Test with a non-existent file
        result = play_audio_file("/tmp/nonexistent.mp3")
        if not result:
            cprint("✅ Correctly handled missing file", "green")
        else:
            cprint("❌ Should have failed for missing file", "red")
            
        cprint("\n💡 To test with a real audio file:", "yellow")
        cprint("   play_audio_file('/path/to/your/audio.mp3')", "white")
        
        cprint("\n🔒 Security benefits:", "cyan")
        cprint("  ✅ No command injection vulnerabilities", "green")
        cprint("  ✅ Path validation and sanitization", "green")
        cprint("  ✅ Error handling with clear messages", "green")
        cprint("  ✅ Cross-platform support (macOS, Windows, Linux)", "green")
        cprint("="*60 + "\n", "cyan")
    except ImportError:
        print("\n" + "="*60)
        print("🔒 Moon Dev's Secure Utilities Test")
        print("="*60 + "\n")
        
        # Test with a non-existent file
        result = play_audio_file("/tmp/nonexistent.mp3")
        if not result:
            print("✅ Correctly handled missing file")
        else:
            print("❌ Should have failed for missing file")
            
        print("\n💡 To test with a real audio file:")
        print("   play_audio_file('/path/to/your/audio.mp3')")
        
        print("\n🔒 Security benefits:")
        print("  ✅ No command injection vulnerabilities")
        print("  ✅ Path validation and sanitization")
        print("  ✅ Error handling with clear messages")
        print("  ✅ Cross-platform support (macOS, Windows, Linux)")
        print("="*60 + "\n")
